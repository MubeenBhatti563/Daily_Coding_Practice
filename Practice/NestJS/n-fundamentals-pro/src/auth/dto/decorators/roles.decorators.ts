import { UserRole } from 'src/user/entities/user.entitiy';
import { SetMetadata } from '@nestjs/common';

export const ROLES_KEY = 'roles';
export const Roles = (...roles: UserRole[]): MethodDecorator =>
  SetMetadata(ROLES_KEY, roles);
