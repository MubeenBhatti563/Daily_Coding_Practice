import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { SongsModule } from './songs/songs.module';
import { HelloModule } from './hello/hello.module';
import { UserModule } from './user/user.module';
import { TestModule } from './test/test.module';
import { PostsModule } from './posts/posts.module';

@Module({
  imports: [
    SongsModule, HelloModule, UserModule, TestModule, PostsModule
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
