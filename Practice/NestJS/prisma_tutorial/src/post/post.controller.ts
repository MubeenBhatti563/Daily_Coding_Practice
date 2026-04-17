import { PostService } from './post.service';
import { CreatePostDto } from './dto/create-post.dto';
import { Body, Controller, Get, Post } from '@nestjs/common';
import { CreateGroupPostDto } from './dto/create-group-post.dto';

@Controller('post')
export class PostController {
  constructor(private readonly postService: PostService) {}

  @Post()
  create(@Body() createPostDto: CreatePostDto) {
    const { userId, ...data } = createPostDto;
    return this.postService.createPost(Number(userId), data);
  }

  @Post('group')
  createGroupPost(@Body() createGroupPostDto: CreateGroupPostDto) {
    const { userId, ...data } = createGroupPostDto;
    return this.postService.createGroupPost(userId.map(Number), data);
  }

  @Get('group')
  getGroupPost() {
    return this.postService.getGroupPost();
  }
}
