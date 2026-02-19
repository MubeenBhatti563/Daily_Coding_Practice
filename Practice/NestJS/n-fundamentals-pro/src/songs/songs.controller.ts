import { Controller, Delete, Get, Post, Put } from '@nestjs/common';

@Controller('songs')
export class SongsController {
  @Post()
  create() {
    return 'Create new song';
  }
  @Get()
  findAll() {
    return 'Find all songs endpoint';
  }
  @Get(':id')
  findOne() {
    return 'Fetch song on the based on id';
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
