import { Injectable, NotFoundException } from '@nestjs/common';
import { Post } from './interfaces/post.interface';
import { NotFoundError } from 'rxjs';
import { InjectRepository } from '@nestjs/typeorm';
import { PostEntity } from './entities/post.entity';
import { Repository } from 'typeorm';
import { CreatePostDto } from './dto/create-post.dto';
import { UpdatePostDto } from './dto/Update-post.dto';

@Injectable()
export class PostsService {
  private posts: Post[] = [
    {
      id: 1,
      title: 'First',
      content: 'First post content',
      authorName: 'M Mubeen',
      createdAt: new Date().toDateString(),
    },
  ];
  constructor(
    @InjectRepository(PostEntity)
    private postsRepository: Repository<PostEntity>,
  ) {}

  async findAll(): Promise<PostEntity[]> {
    return this.postsRepository.find();
  }

  async findOne(id: number): Promise<PostEntity> {
    const post = await this.postsRepository.findOneBy({ id });
    if (!post) throw new NotFoundException(`Post with ID ${id} is not found`);
    return post;
  }

  async createPost(createPostData: CreatePostDto): Promise<PostEntity> {
    const newPost = this.postsRepository.create({
      title: createPostData.title,
      content: createPostData.content,
      authorName: createPostData.authorName,
    });
    return this.postsRepository.save(newPost);
  }

  async updatePost(id: number, updatePost: UpdatePostDto): Promise<PostEntity> {
    const findPost = await this.findOne(id);
    if (findPost.title) {
      findPost.title = updatePost.title;
    }
    if (findPost.content) {
      findPost.content = updatePost.content;
    }
    if (findPost.authorName) {
      findPost.authorName = updatePost.authorName;
    }
    return this.postsRepository.save(findPost);
  }
  async deletePost(id: number): Promise<void> {
    const findPostDelete = await this.findOne(id);
    await this.postsRepository.remove(findPostDelete);
  }
}
