import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { SongsModule } from './songs/songs.module';
import { HelloModule } from './hello/hello.module';

@Module({
  imports: [SongsModule, HelloModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
