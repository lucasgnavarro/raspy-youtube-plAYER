import pyglet
import os


class AudioPlayer(object):

    file_name = ''
    length_file = 0
    current_time_position = 0

    def play_audio_file(self, file_name=None):
        self.clear_vars()
        print 'FileName : %s' % file_name
        if file_name:
            self.file_name = file_name
        else:
            raise Exception('Invalid filename')

        try:
            os.stat(self.file_name)
            song = pyglet.media.load(self.file_name)
            song.play()
            self.length_file = song.duration

            pyglet.clock.schedule_once(self.detroy_current_player, self.length_file)
            #pyglet.clock.schedule_interval(self.show_current_song_time, 1.0)
            print 'Playing {filename}'.format(filename=self.file_name)
            pyglet.app.run()

        except OSError:
            raise Exception('Sorry, i cannot read the specified filename')

    def detroy_current_player(self, dt):
        pyglet.app.exit()

    def show_current_song_time(self, dt):
        self.current_time_position += 1
        print 'Playing {filename} : {current} / {total} \r'.format(filename=self.file_name,
                                                                   current=self.current_time_position,
                                                                   total=self.length_file)

    def clear_vars(self):
        file_name = ''
        length_file = 0
        current_time_position = 0


#
# def play_audio_file(file_name=None):
#     if file_name:
#         time_rep = 0
#         total_time_song = 0
#         try:
#             os.stat(file_name)
#             song = pyglet.media.load(file_name)
#             print 'Reproduciendo %s' % file_name
#             song.play()
#             total_time_song = song.duration
#             pyglet.clock.schedule_once(exiter, total_time_song)
#             pyglet.clock.schedule_interval(show_current_song_time, 1.0)
#             pyglet.app.run()
#
#         except OSError:
#             print 'Error el archivo no existe'
#
#
#
#

