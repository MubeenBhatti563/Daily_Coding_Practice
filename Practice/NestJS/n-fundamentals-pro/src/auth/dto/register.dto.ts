import {
  IsEmail,
  IsNotEmpty,
  IsString,
  IsStrongPassword,
  MaxLength,
  MinLength,
} from 'class-validator';

export class RegisterDto {
  @IsEmail({}, { message: 'Please provide a valid email' })
  email: string;

  @IsString()
  @IsNotEmpty()
  @MaxLength(15, { message: 'Username not exceed 15 chars' })
  @MinLength(4, { message: 'Username should be atleast 4' })
  username: string;

  @IsString({ message: 'Password must be combination of strings!' })
  @IsNotEmpty()
  @IsStrongPassword()
  password: string;
}
