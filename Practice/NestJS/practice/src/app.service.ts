import { Injectable, NotFoundException } from '@nestjs/common';
import { ProductEntity } from './entities/product.entity';
import { Repository } from 'typeorm';
import { InjectRepository } from '@nestjs/typeorm';
import { ProductDto } from './dto/product.dto';

@Injectable()
export class AppService {
  constructor(
    @InjectRepository(ProductEntity)
    private productRepository: Repository<ProductEntity>,
  ) {}

  getHello(): string {
    return 'Hello World!';
  }

  async getProducts(): Promise<ProductEntity[]> {
    return this.productRepository.find();
  }

  async getProduct(id: number): Promise<ProductEntity | null> {
    const product = await this.productRepository.findOneBy({ id });
    if (!product)
      throw new NotFoundException(`Product with id ${id} is not found!`);
    return product;
  }

  async postProduct(productDto: ProductDto): Promise<ProductEntity> {
    const product = this.productRepository.create({
      name: productDto.name,
      quantity: productDto.quantity,
      sales: productDto.sales,
      price: productDto.price,
      description: productDto.description,
    });
    return this.productRepository.save(product);
  }

  async updateProduct(
    id: number,
    productDto: ProductDto,
  ): Promise<ProductEntity> {
    await this.productRepository.update(
      { id },
      {
        name: productDto.name,
        quantity: productDto.quantity,
        sales: productDto.sales,
        price: productDto.price,
        description: productDto.description,
      },
    );
    const updatedProduct = await this.productRepository.findOneBy({ id });
    if (!updatedProduct)
      throw new NotFoundException(`Product with id ${id} is not found!`);
    return updatedProduct;
  }

  async deleteProduct(id: number): Promise<void> {
    const item = await this.productRepository.findOneBy({ id });
    if (!item) {
      throw new NotFoundException(`Product with id ${id} is not found!`);
    }
    await this.productRepository.delete(item);
  }
}
