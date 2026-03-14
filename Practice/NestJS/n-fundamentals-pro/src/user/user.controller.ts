import { UserService } from './user.service';
import {
  Body,
  ClassSerializerInterceptor,
  Controller,
  Delete,
  Get,
  HttpCode,
  HttpStatus,
  Param,
  ParseIntPipe,
  Post,
  Put,
  UseInterceptors,
} from '@nestjs/common';
import { UserEntity } from './entities/user.entitiy';
import { UserDto } from './dto/user.dto';

@Controller('user')
@UseInterceptors(ClassSerializerInterceptor)
export class UserController {
  constructor(private readonly userService: UserService) {}
  @Get()
  async getNames(): Promise<UserEntity[]> {
    return this.userService.getAllUsers();
  }

  @Get(':id')
  async getUserById(
    @Param('id', ParseIntPipe) id: number,
  ): Promise<UserEntity> {
    return this.userService.getUserById(id);
  }

  @Get('hello/:id')
  async getUserGreet(@Param('id', ParseIntPipe) id: number): Promise<string> {
    return this.userService.getHelloName(id);
  }

  @Post()
  @HttpCode(HttpStatus.CREATED)
  async createUser(@Body() userData: UserDto): Promise<UserEntity> {
    return this.userService.postUser(userData);
  }

  @Put(':id')
  async updateUser(
    @Param('id', ParseIntPipe) id: number,
    @Body() userData: UserDto,
  ): Promise<UserEntity> {
    return this.userService.updateUser(id, userData);
  }

  @Delete(':id')
  @HttpCode(HttpStatus.NO_CONTENT)
  async deleteUser(@Param('id', ParseIntPipe) id: number): Promise<void> {
    await this.userService.deleteUser(id);
  }
}
