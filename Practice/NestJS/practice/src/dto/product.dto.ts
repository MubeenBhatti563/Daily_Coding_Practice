import {
  IsInt,
  IsNotEmpty,
  IsString,
  MaxLength,
  MinLength,
} from 'class-validator';

export class ProductDto {
  @IsNotEmpty()
  @IsString()
  @MaxLength(15, { message: 'Not exceed 15 characters' })
  @MinLength(5, { message: 'Min length should be 5 characters' })
  name: string;

  @IsNotEmpty()
  @IsInt()
  quantity: number;

  @IsInt()
  @IsNotEmpty()
  sales: number;

  @IsInt()
  @IsNotEmpty()
  price: number;

  @IsString()
  description: string;
}

export interface ProductInterface {
  id: number;
  name: string;
  quantity: number;
  sales: number;
  price: number;
  description: string;
}
