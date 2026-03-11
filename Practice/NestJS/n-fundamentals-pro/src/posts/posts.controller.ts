import {
  Body,
  Controller,
  Delete,
  Get,
  HttpCode,
  HttpStatus,
  Param,
  ParseIntPipe,
  Post,
  Put,
  Query,
  UsePipes,
  ValidationPipe,
} from '@nestjs/common';
import { PostsService } from './posts.service';
import type { Post as InterfacePost } from './interfaces/post.interface';
import { CreatePostDto } from './dto/create-post.dto';

@Controller('posts')
export class PostsController {
  constructor(private readonly postService: PostsService) {}
  @Get()
  findAll(@Query('search') search: string): InterfacePost[] {
    const extractPosts = this.postService.findAll();
    if (search) {
      return extractPosts.filter((posts) =>
        posts.title.toLowerCase().includes(search.toLowerCase()),
      );
    }
    return extractPosts;
  }
  @Get(':id')
  findOne(@Param('id', ParseIntPipe) id: number): InterfacePost {
    return this.postService.findOne(id);
  }
  @Post()
  @HttpCode(HttpStatus.CREATED)
  // @UsePipes(
  //   new ValidationPipe({
  //     whitelist: true,
  //     forbidNonWhitelisted: true,
  //     transform: true,
  //     disableErrorMessages: false,
  //   }),
  // )
  create(@Body() createPostData: CreatePostDto): InterfacePost {
    return this.postService.createPost(createPostData);
  }
  @Put(':id')
  update(
    @Param('id', ParseIntPipe) id: number,
    @Body() updatePostData: Partial<Omit<InterfacePost, 'id' | 'createdAt'>>,
  ): InterfacePost {
    return this.postService.updatePost(id, updatePostData);
  }
  @Delete(':id')
  deletePost(@Param('id', ParseIntPipe) id: number): void {
    this.postService.deletePost(id);
  }
}
