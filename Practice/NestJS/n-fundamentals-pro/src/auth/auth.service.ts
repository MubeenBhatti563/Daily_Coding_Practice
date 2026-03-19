import { RegisterDto } from './dto/register.dto';
import {
  ConflictException,
  Injectable,
  UnauthorizedException,
} from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { UserEntity, UserRole } from 'src/user/entities/user.entitiy';
import { Repository } from 'typeorm';
import * as bcrypt from 'bcrypt';
import { JwtService } from '@nestjs/jwt';

@Injectable()
export class AuthService {
  constructor(
    @InjectRepository(UserEntity)
    private userRepository: Repository<UserEntity>,
    private jwtService: JwtService,
  ) {}

  private async getHashPassword(password: string): Promise<string> {
    // Making password encrypted
    const salt = await bcrypt.genSalt();
    const hashPassword = await bcrypt.hash(password, salt);
    return hashPassword;
  }

  async register(regsiterDto: RegisterDto) {
    const existingUser = await this.userRepository.findOne({
      where: { email: regsiterDto.email },
    });

    if (existingUser) {
      throw new ConflictException(
        'Email already in use! Please try with a diff email!',
      );
    }

    const hashPassword = await this.getHashPassword(regsiterDto.password);
    const newUser = await this.userRepository.create({
      email: regsiterDto.email,
      username: regsiterDto.username,
      password: hashPassword,
      role: UserRole.USER,
    });
    const savedUser = await this.userRepository.save(newUser);
    const { password, ...result } = savedUser;

    return {
      user: result,
      message: 'Registration successfully!',
    };
  }

  async createAdmin(registerDto: RegisterDto) {
    const existingUser = await this.userRepository.findOne({
      where: { email: registerDto.email },
    });
    if (existingUser) {
      throw new ConflictException(
        'This email is already in use! Try another please!',
      );
    }
    const hashPassword = await this.getHashPassword(registerDto.password);
    const newAdmin = await this.userRepository.create({
      email: registerDto.email,
      username: registerDto.username,
      password: hashPassword,
      role: UserRole.ADMIN,
    });
    const savedAdmin = await this.userRepository.save(newAdmin);
    const { password, ...result } = savedAdmin;
    return {
      admin: result,
      message: 'Admin created Successfully!',
    };
  }

  async loginUser(registerDto: RegisterDto) {
    const user = await this.userRepository.findOne({
      where: { email: registerDto.email },
    });

    if (
      !user ||
      !(await this.verifyPassword(registerDto.password, user.password))
    ) {
      throw new UnauthorizedException(
        'Invalid credentials or accout not exists',
      );
    }
    // Generate Tokens
    const tokens = await this.generateToken(user);
    const { password, ...result } = user;
    return {
      user: result,
      ...tokens,
    };
  }

  private async verifyPassword(
    plainPassword: string,
    hashPassword: string,
  ): Promise<boolean> {
    return bcrypt.compare(plainPassword, hashPassword);
  }

  private async generateToken(user: UserEntity) {
    return {
      accessToken: this.generateAccessToken(user),
      refreshToken: this.generateRefreshToken(user),
    };
  }
  private async refreshToken(refreshToken: string) {
    try {
      const payload = this.jwtService.verify(refreshToken, {
        secret: 'refresh_secret',
      });
      const user = await this.userRepository.findOne({
        where: { id: payload.sub },
      });

      if (!user) {
        throw new UnauthorizedException('Invalid token');
      }
      const accessToken = this.generateAccessToken(user);
      return { accessToken };
    } catch (e) {
      throw new UnauthorizedException('Invalid token');
    }
  }
  private generateAccessToken(user: UserEntity): string {
    const payload = {
      email: user.email,
      sub: user.id,
      role: user.role,
    };

    return this.jwtService.sign(payload, {
      secret: 'jwt_secret',
      expiresIn: '15m',
    });
  }
  private generateRefreshToken(user: UserEntity): string {
    const payload = {
      sub: user.id,
    };

    return this.jwtService.sign(payload, {
      secret: 'refresh_secret',
      expiresIn: '2d',
    });
  }
}
