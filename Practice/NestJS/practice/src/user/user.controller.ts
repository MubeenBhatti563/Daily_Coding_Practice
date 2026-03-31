import {
  Body,
  Controller,
  Get,
  HttpCode,
  HttpStatus,
  Param,
  ParseIntPipe,
  Post,
  UseGuards,
} from '@nestjs/common';
import { UserService } from './user.service';
import { UserEntity } from 'src/entities/user.entity';
import { UserDto } from 'src/dto/user.dto';
import { AuthGuard } from '@nestjs/passport';

@Controller('user')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Get()
  @HttpCode(HttpStatus.ACCEPTED)
  async getUsers() {
    return this.userService.getUsers();
  }

  @UseGuards(AuthGuard('jwt'))
  @Get(':id')
  async getUser(@Param('id', ParseIntPipe) id: number): Promise<UserEntity> {
    return this.userService.getUser(id);
  }

  @Post()
  async createUser(@Body() userDto: UserDto): Promise<UserEntity> {
    return this.userService.createUser(userDto);
  }
}
