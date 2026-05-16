import {
  IsNotEmpty,
  IsOptional,
  IsString,
  MaxLength,
  MinLength,
} from 'class-validator';

export class UpdatePostDto {
  @IsOptional()
  @IsNotEmpty({ message: 'Title is requied!' })
  @IsString({ message: 'Title must be a string!' })
  @MinLength(3, { message: 'Title must be 3 characters long!' })
  @MaxLength(50, { message: 'Title must not exceed 50 chars' })
  title: string;

  @IsOptional()
  @IsNotEmpty({ message: 'Content is requied!' })
  @IsString({ message: 'Content must be a string!' })
  @MinLength(10, { message: 'Content must be 10 characters long!' })
  content: string;

  @IsOptional()
  @IsNotEmpty({ message: 'AuthorName is requied!' })
  @IsString({ message: 'AuthorName must be a string!' })
  @MinLength(3, { message: 'AuthorName must be 3 characters long!' })
  @MaxLength(50, { message: 'AuthorName must not exceed 50 chars' })
  authorName: string;
}
