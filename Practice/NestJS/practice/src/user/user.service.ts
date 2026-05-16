import {
  ConflictException,
  Injectable,
  NotFoundException,
} from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { UserDto } from 'src/dto/user.dto';
import { UserEntity } from 'src/entities/user.entity';
import { Repository } from 'typeorm';
import * as bcrypt from 'bcrypt';

@Injectable()
export class UserService {
  constructor(
    @InjectRepository(UserEntity)
    private userRepository: Repository<UserEntity>,
  ) {}

  async getUsers(): Promise<UserEntity[]> {
    return this.userRepository.find();
  }

  async getUser(id: number): Promise<UserEntity> {
    const user = await this.userRepository.findOneBy({ id });
    if (!user) throw new NotFoundException(`User with id ${id} not found!`);
    return user;
  }

  async createUser(userDto: UserDto): Promise<UserEntity> {
    const existingUser = await this.findOneByEmail(userDto.email);
    if (existingUser) throw new ConflictException('Email already exists');
    const { password, ...userData } = userDto;
    const hashPassword = await this.getHashPassword(password);
    const newUser = this.userRepository.create({
      ...userData,
      password: hashPassword,
    });
    return this.userRepository.save(newUser);
  }

  private async getHashPassword(password: string): Promise<string> {
    const salt = await bcrypt.genSalt();
    const hashPassword = await bcrypt.hash(password, salt);
    return hashPassword;
  }

  async findOneByEmail(email: string): Promise<UserEntity | null> {
    return this.userRepository.findOne({ where: { email } });
  }
}
