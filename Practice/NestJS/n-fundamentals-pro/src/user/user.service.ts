import { InjectRepository } from '@nestjs/typeorm';
import { Injectable, NotFoundException } from '@nestjs/common';
import { HelloService } from '../hello/hello.service';
import { UserEntity } from './entities/user.entitiy';
import { Repository } from 'typeorm';
import { UserDto } from './dto/user.dto';
import * as bcrypt from 'bcrypt';

@Injectable()
export class UserService {
  constructor(
    @InjectRepository(UserEntity)
    private readonly userRepository: Repository<UserEntity>,
    private readonly helloService: HelloService,
  ) {}

  async getAllUsers(): Promise<UserEntity[]> {
    return this.userRepository.find();
  }

  async getUserById(id: number): Promise<UserEntity> {
    const user = await this.userRepository.findOneBy({ id });
    if (!user) throw new NotFoundException(`User with ID ${id} is not found`);
    return user;
  }

  async postUser(userData: UserDto): Promise<UserEntity> {
    const hashPassword = await this.getHashPassword(userData.password);
    const newUser = await this.userRepository.create({
      ...userData,
      password: hashPassword,
    });

    return this.userRepository.save(newUser);
  }

  async getHashPassword(password: string): Promise<string> {
    // Making password encrypted
    const salt = await bcrypt.genSalt();
    const hashPassword = await bcrypt.hash(password, salt);
    return hashPassword;
  }

  async deleteUser(id: number): Promise<void> {
    const userInfo = await this.getUserById(id);
    await this.userRepository.remove(userInfo);
  }

  async updateUser(id: number, userData: UserDto): Promise<UserEntity> {
    const userInfo = await this.getUserById(id);
    if (userInfo.username) userInfo.username = userData.username;
    if (userInfo.email) userInfo.email = userData.email;
    if (userInfo.password)
      userInfo.password = await this.getHashPassword(userData.password);

    return this.userRepository.save(userInfo);
  }

  async getHelloName(id: number): Promise<string> {
    const user = await this.getUserById(id);
    if (!user) {
      return 'User not found!';
    } else {
      return this.helloService.getHelloName(user?.username);
    }
  }
}
