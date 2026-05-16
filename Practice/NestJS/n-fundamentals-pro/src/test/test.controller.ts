import { Controller, Get } from '@nestjs/common';
import { UserService } from '../user/user.service';

@Controller('test')
export class TestController {
  constructor(private readonly userService: UserService) {}
  @Get()
  getUsers() {
    return this.userService.getAllUsers();
  }
}
