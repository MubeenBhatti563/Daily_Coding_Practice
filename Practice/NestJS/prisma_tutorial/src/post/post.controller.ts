import { PostService } from './post.service';
import { CreatePostDto } from './dto/create-post.dto';
import { Body, Controller, Post } from '@nestjs/common';

@Controller('post')
export class PostController {
  constructor(private readonly postService: PostService) {}

  @Post()
  create(@Body() createPostDto: CreatePostDto) {
    const { userId, ...data } = createPostDto;
    return this.postService.createPost(Number(userId), data);
  }
}
