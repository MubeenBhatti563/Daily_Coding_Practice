import { Injectable, UnauthorizedException } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import { UserService } from 'src/user/user.service';
import * as bcrypt from 'bcrypt';

@Injectable()
export class AuthService {
  constructor(
    private readonly userService: UserService,
    private readonly jwtService: JwtService,
  ) {}

  async login(email: string, password: string) {
    const user = await this.userService.findOneByEmail(email);
    const isMatch = await bcrypt.compare(password, user?.password || '');

    if (!isMatch) {
      throw new UnauthorizedException('Invalid credentials!');
    }
    // TODO: validate password and generate JWT token
    const payload = { sub: user?.id, email: user?.email };
    return {
      access_token: await this.jwtService.signAsync(payload),
      user: { id: user?.id, username: user?.username },
    };
  }
}
