import logging


class InsertSort(object):
    logging.basicConfig(level=logging.DEBUG)

    @staticmethod
    def sort(array):
        assert isinstance(array, list), 'should be array'
        assert len(array) > 0, 'lentgh should be more than 0'
        logging.debug("Input array is {}", array)

        for currentIndex in range(1, len(array)):
            key = array[currentIndex]
            prevIndex = currentIndex - 1
            logging.debug("Current index = {}, value {}", currentIndex, key)

            while prevIndex >= 0 and array[prevIndex] > key:
                logging.debug("\t Value under index {} is bigger: {} > {}", prevIndex, array[prevIndex], key)
                array[prevIndex + 1] = array[prevIndex]
                prevIndex -= 1

            logging.debug("\t Current index value ({}) is moved to {}", key, prevIndex + 1)
            array[prevIndex + 1] = key
