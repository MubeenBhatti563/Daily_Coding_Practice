// src/prisma/prisma.service.ts
import { Injectable, OnModuleInit, OnModuleDestroy } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';
import { PrismaPg } from '@prisma/adapter-pg';
import { Pool } from 'pg';

@Injectable()
export class PrismaService
  extends PrismaClient
  implements OnModuleInit, OnModuleDestroy
{
  constructor() {
    // 1. Create a standard 'pg' pool using your env variable
    const pool = new Pool({ connectionString: process.env.DATABASE_URL });

    // 2. Create the Prisma adapter
    const adapter = new PrismaPg(pool);

    // 3. Pass the adapter to the super constructor
    super({ adapter });
  }

  async onModuleInit() {
    await this.$connect();
    console.log('Connected to DB successfully!');
  }

  async onModuleDestroy() {
    await this.$disconnect();
  }
}
