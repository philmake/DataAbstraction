
class Ball:

    def __init__(self):
        self.__speed = 0
        pass

    def set_speed(self, speed=0):
        self.__speed = speed
        pass

    def get_speed(self):
        return self.__speed

    pass


class Game:

    #@staticmethod
    def play_game(self):
        mball = Ball()
        mball.set_speed(10)
        print("mball: {}".format(mball.get_speed()))
        self.pass_ball(mball)
        print("mball: {}".format(mball.get_speed()))
        mball.set_speed(30)
        print("mball: {}".format(mball.get_speed()))
        pass

    def pass_ball(self, nball=Ball):
        nball.set_speed(nball.get_speed() + 5)
        self.catch_ball(nball)
        pass

    def catch_ball(self, nball=Ball):
        n2ball = Ball()
        n2ball.set_speed(40)
        n2ball.set_speed(0)
        nball = n2ball
        print(nball, n2ball)
        print("nball: {}".format(nball.get_speed()))
        print("Caught the ball!")

    pass


game = Game()
game.play_game()
