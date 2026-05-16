import {
  IsEmail,
  IsNotEmpty,
  IsString,
  IsStrongPassword,
} from 'class-validator';

export class LoginDto {
  @IsEmail({}, { message: 'Please provide a valid email' })
  email: string;

  @IsString({ message: 'Password must be combination of strings!' })
  @IsNotEmpty()
  @IsStrongPassword()
  password: string;
}
