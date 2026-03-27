import {
  Body,
  Controller,
  Get,
  HttpCode,
  HttpStatus,
  Param,
  ParseIntPipe,
  Post,
} from '@nestjs/common';
import { AppService } from './app.service';
import { ProductEntity } from './entities/product.entity';
import { ProductDto } from './dto/product.dto';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  @HttpCode(HttpStatus.ACCEPTED)
  async getProducts(): Promise<ProductEntity[]> {
    return this.appService.getProducts();
  }

  @Get(':id')
  @HttpCode(HttpStatus.ACCEPTED)
  async getProduct(
    @Param('id', ParseIntPipe) id: number,
  ): Promise<ProductEntity | null> {
    return this.appService.getProduct(id);
  }

  @Post()
  @HttpCode(HttpStatus.CREATED)
  async createProduct(@Body() productDto: ProductDto): Promise<ProductEntity> {
    return this.appService.postProduct(productDto);
  }
}
