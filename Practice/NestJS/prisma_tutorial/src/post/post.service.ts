import { Injectable } from '@nestjs/common';
import { CreatePostDto } from './dto/create-post.dto';
import { PrismaService } from 'src/prisma/prisma.service';

@Injectable()
export class PostService {
  constructor(private prisma: PrismaService) {}
  createPost(userId: number, data: CreatePostDto) {
    return this.prisma.post.create({
      data: {
        title: data.title || '',
        description: data.description || '',
        userId,
      },
    });
  }
}
