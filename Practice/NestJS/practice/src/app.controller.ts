import {
  Body,
  Controller,
  Delete,
  Get,
  HttpCode,
  HttpStatus,
  Param,
  ParseIntPipe,
  Post,
  Put,
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
  @HttpCode(HttpStatus.OK)
  async getProduct(
    @Param('id', ParseIntPipe) id: number,
  ): Promise<ProductEntity | null> {
    return this.appService.getProduct(id);
  }

  @Post()
  @HttpCode(HttpStatus.OK)
  async createProduct(@Body() productDto: ProductDto): Promise<ProductEntity> {
    return this.appService.postProduct(productDto);
  }

  @Put(':id')
  @HttpCode(HttpStatus.ACCEPTED)
  async updateProduct(
    @Param('id', ParseIntPipe) id: number,
    @Body() productDto: ProductDto,
  ): Promise<ProductEntity> {
    return this.appService.updateProduct(id, productDto);
  }

  @Delete(':id')
  @HttpCode(HttpStatus.NO_CONTENT)
  async deleteProduct(@Param('id', ParseIntPipe) id: number): Promise<void> {
    await this.appService.deleteProduct(id);
  }
}
