import { UserService } from './user.service';
import { Controller, Get, Param, ParseIntPipe } from '@nestjs/common';
import { HelloService } from 'src/hello/hello.service';

@Controller('user')
export class UserController {
  constructor(private readonly userService: UserService) {}
  @Get()
  getNames() {
    return this.userService.getAllUsers();
  }
  @Get(':id')
  getUserbyId(@Param('id', ParseIntPipe) id: number) {
    return this.userService.getUserbyId(id);
  }
  @Get('hello/:id')
  getUserGreet(@Param('id', ParseIntPipe) id: number): string {
    return this.userService.getHelloName(id);
  }
}
