from math import sqrt

class LP:
    # Deposit `initial` of ETH, and set the PRT at +`delta`%
    # of current price to cost `price`
    def __init__(self, initial, delta, price, a):
        self.I = I = initial
        self.D = D = delta
        self.Da = Da = delta ** a
        self.P = P = price
        self.a = a = a

        # compute parameters
        y = (P * (I+1)) / (P+1)
        y_D = y
        x_D = I - y_D
        k_D = x_D * y_D

        self.b = (I**2) / 4
        self.m = (1/Da) * (k_D-self.b)

    def prices_at_deltas(self, upper_delta=100):
        results = []

        for delta in range(0, upper_delta, 1):
            delta_a = delta ** self.a
            k = self.m * delta_a + self.b
            x = (-self.I + sqrt(self.I*self.I - 4*k)) / -2
            y = (-self.I - sqrt(self.I*self.I - 4*k)) / -2

            delta_x = self.I / 100.0
            delta_y = -(k / (delta_x + x) - y)

            price = delta_y / delta_x

            if price < 0:
                continue
            if price > 10:
                continue

            result = {'delta': delta, 'delta_a': delta_a, 'price': price}
            results.append(result)

        return results


def run():
    lp = LP(100, 10, 1.05, 1)

    print('b=', lp.b)
    print('m=', lp.m)

    results = lp.prices_at_deltas()

if __name__ == '__main__':
    run()
