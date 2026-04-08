import { IsBoolean, IsOptional } from 'class-validator';

export class UpdateUserSettingDto {
  @IsOptional()
  @IsBoolean()
  smsEnabled?: boolean;

  @IsOptional()
  @IsBoolean()
  notificationsOn?: boolean;
}
