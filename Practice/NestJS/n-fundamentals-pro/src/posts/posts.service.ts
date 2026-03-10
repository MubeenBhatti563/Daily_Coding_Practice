import { Injectable, NotFoundException } from '@nestjs/common';
import { Post } from './interfaces/post.interface';
import { NotFoundError } from 'rxjs';

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
  findAll(): any {
    return this.posts;
  }
  findOne(id: number): Post {
    const post = this.posts.find((p) => p.id === id);
    if (!post) throw new NotFoundException(`Post with ID ${id} is not found`);
    return post;
  }
  createPost(createPostData: Omit<Post, 'id' | 'createdAt'>): Post {
    const newPost: Post = {
      id: this.getNextId(),
      ...createPostData,
      createdAt: new Date().toDateString(),
    };
    this.posts.push(newPost);
    return newPost;
  }
  getNextId(): number {
    return this.posts.length === 0
      ? 1
      : Math.max(...this.posts.map((p) => p.id)) + 1;
  }
  updatePost(
    id: number,
    updatePost: Partial<Omit<Post, 'id' | 'createdAt'>>,
  ): Post {
    const indexNumber = this.posts.findIndex((p) => p.id === id);
    if (indexNumber === -1) {
      throw new NotFoundException(`Post with ID ${id} is not found`);
    }
    this.posts[indexNumber] = {
      ...this.posts[indexNumber],
      ...updatePost,
      updatedAt: new Date(),
    };
    return this.posts[indexNumber];
  }
  deletePost(id: number): { message: string } {
    const indexNumber = this.posts.findIndex((p) => p.id === id);
    if (indexNumber === -1) {
      throw new NotFoundException(`Post with ID ${id} is not found`);
    }
    this.posts.splice(indexNumber, 1);
    return { message: `Post with ID ${id} has been deleted!` };
  }
}
