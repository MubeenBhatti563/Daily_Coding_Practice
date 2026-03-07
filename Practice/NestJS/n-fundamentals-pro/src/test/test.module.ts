import { Module } from '@nestjs/common';
import { TestService } from './test.service';
import { TestController } from './test.controller';
import { UserModule } from 'src/user/user.module';

@Module({
  imports: [UserModule],
  providers: [TestService],
  controllers: [TestController],
})
export class TestModule {}
