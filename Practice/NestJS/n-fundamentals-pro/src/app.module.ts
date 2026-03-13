import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { SongsModule } from './songs/songs.module';
import { HelloModule } from './hello/hello.module';
import { UserModule } from './user/user.module';
import { TestModule } from './test/test.module';
import { PostsModule } from './posts/posts.module';
import { TypeOrmModule } from '@nestjs/typeorm';
import { PostEntity } from './posts/entities/post.entity';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: 'localhost',
      port: 5432,
      username: 'postgres',
      password: 'ali123',
      database: 'YoutubePosts',
      entities: [PostEntity],
      synchronize: true,
    }),
    SongsModule,
    HelloModule,
    UserModule,
    TestModule,
    PostsModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
