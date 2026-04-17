import { Injectable } from '@nestjs/common';
import { CreatePostDto } from './dto/create-post.dto';
import { PrismaService } from 'src/prisma/prisma.service';
import { Prisma } from '@prisma/client';

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

  createGroupPost(usersId: number[], data: Prisma.GroupPostCreateInput) {
    return this.prisma.groupPost.create({
      data: {
        ...data,
        users: {
          create: usersId.map((id) => ({
            userId: id,
          })),
        },
      },
    });
  }

  getGroupPost() {
    return this.prisma.groupPost.findMany({
      include: {
        users: {
          select: {
            user: true,
          },
        },
      },
    });
  }
}
