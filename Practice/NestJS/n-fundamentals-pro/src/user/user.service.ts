import { Injectable } from '@nestjs/common';
import { HelloService } from 'src/hello/hello.service';

@Injectable()
export class UserService {
  constructor(private readonly helloService: HelloService) {}
  getAllUsers() {
    return [
      {
        id: 1,
        name: 'Mubeen',
      },
      {
        id: 2,
        name: 'Rizwan',
      },
      {
        id: 3,
        name: 'Marwa',
      },
    ];
  }
  getUserbyId(id: number) {
    const user = this.getAllUsers().find((user) => user.id === id);
    return user;
  }
  getHelloName(id: number) {
    const user = this.getUserbyId(id);
    if (!user) {
      return 'User not found!';
    } else {
      return this.helloService.getHelloName(user?.name);
    }
  }
}
