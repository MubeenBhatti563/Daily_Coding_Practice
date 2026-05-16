import { Injectable } from '@nestjs/common';

export interface Song {
  id: number;
  title: string;
  artists: string[];
  releaseDate: Date;
  duration: string;
}

@Injectable()
export class SongsService {
  private readonly songs: Song[] = [];
  create(song: Omit<Song, 'id'>): Song {
    const newSong = {
      id: this.songs.length + 1,
      ...song,
    };
    this.songs.push(newSong);
    return newSong;
  }
  findAll(): Song[] {
    return this.songs;
  }
  findOne(id: number): Song | undefined {
    return this.songs.find((song) => song.id === id);
  }
}
