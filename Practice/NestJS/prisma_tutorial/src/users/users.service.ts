import {
  ConflictException,
  Injectable,
  NotFoundException,
} from '@nestjs/common';
import { PrismaService } from 'src/prisma/prisma.service';
import { Prisma } from '@prisma/client';
import { UserDto } from './dtos/users.dto';
import { UpdateUserSettingDto } from './dtos/updateusersetting.dto';

@Injectable()
export class UsersService {
  constructor(private readonly prisma: PrismaService) {}

  async getUsers() {
    const users = await this.prisma.user.findMany({
      include: { userSetting: true },
    });
    console.log('Users with settings:', JSON.stringify(users, null, 2));
    return users;
  }

  async createUser(dto: UserDto) {
    try {
      return await this.prisma.user.create({
        data: {
          ...dto,
          userSetting: {
            create: {
              smsEnabled: true,
              notificationsOn: false,
            },
          },
        },
      });
    } catch (error) {
      if (
        error instanceof Prisma.PrismaClientKnownRequestError &&
        error.code === 'P2002'
      ) {
        throw new ConflictException('Username or Email already exists');
      }
      throw error;
    }
  }

  async getUserById(id: number) {
    const user = await this.prisma.user.findUnique({
      where: { id },
      include: {
        userSetting: {
          select: {
            smsEnabled: true,
            notificationsOn: true,
          },
        },
      },
    });

    if (!user) throw new NotFoundException('User not found');
    return user;
  }

  async updateUser(id: number, dto: UserDto) {
    await this.getUserById(id);

    try {
      return await this.prisma.user.update({
        where: { id },
        data: dto,
      });
    } catch (error) {
      if (
        error instanceof Prisma.PrismaClientKnownRequestError &&
        error.code === 'P2002'
      ) {
        throw new ConflictException('Username or Email already exists');
      }
      throw error;
    }
  }

  async deleteUser(id: number) {
    await this.getUserById(id);
    await this.prisma.user.delete({ where: { id } });
  }

  async updateUserSetting(
    id: number,
    updateUserSettingDto: UpdateUserSettingDto,
  ) {
    await this.getUserById(id);
    return this.prisma.userSetting.update({
      where: { id },
      data: updateUserSettingDto,
    });
  }
}
