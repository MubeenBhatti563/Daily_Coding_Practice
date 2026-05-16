import { Injectable } from '@nestjs/common';

@Injectable()
export class HelloService {
  getHello(): string {
    return "Hello Nest JS! I'm Mubeen!";
  }
  getHelloName(name: string): string {
    return `Hello ${name}`;
  }
}
