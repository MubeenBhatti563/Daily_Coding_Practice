import { Controller, Get, Param, Query } from '@nestjs/common';
import { HelloService } from './hello.service';

// incoming requests and returning responces
// get, post, put and delete etc
@Controller('hello')
export class HelloController {
  constructor(private readonly helloService: HelloService) {}
  @Get()
  getHello(): string {
    return this.helloService.getHello();
  }
  @Get('user/:name')
  getHelloName(@Param('name') name: string): string {
    return this.helloService.getHelloName(name);
  }
  @Get('query')
  getQueryName(@Query('name') name: string): string {
    return this.helloService.getHelloName(name || 'world');
  }
}
