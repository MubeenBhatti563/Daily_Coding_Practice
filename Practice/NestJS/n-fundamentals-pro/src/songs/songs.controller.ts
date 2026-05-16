import { CreateSongDTO } from './dto/create-song-dto';
import { SongsService } from './songs.service';
import {
  Body,
  Controller,
  Delete,
  Get,
  Param,
  ParseIntPipe,
  Post,
  Put,
} from '@nestjs/common';

@Controller('songs')
export class SongsController {
  constructor(private SongsService: SongsService) {}
  @Post()
  create(@Body() createSongDTO: CreateSongDTO) {
    return this.SongsService.create(createSongDTO);
  }
  @Get()
  findAll() {
    return this.SongsService.findAll();
  }
  @Get(':id')
  findOne(@Param('id', ParseIntPipe) id: number) {
    return this.SongsService.findOne(id);
  }
  @Put(':id')
  update() {
    return 'Update song on the based on id';
  }
  @Delete(':id')
  delete() {
    return 'Delete song on the based on id';
  }
}
