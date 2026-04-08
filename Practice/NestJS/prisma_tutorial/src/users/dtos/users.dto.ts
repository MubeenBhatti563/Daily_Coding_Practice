import { IsNotEmpty, IsOptional, IsString } from 'class-validator';

export class UserDto {
  @IsString()
  @IsNotEmpty()
  username: string;

  @IsString()
  @IsOptional()
  displayName?: string;
}
