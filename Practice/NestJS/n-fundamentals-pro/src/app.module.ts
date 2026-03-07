import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { SongsModule } from './songs/songs.module';
import { HelloModule } from './hello/hello.module';
import { UserModule } from './user/user.module';
import { TestModule } from './test/test.module';

@Module({
  imports: [
    SongsModule, HelloModule, UserModule, TestModule
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
