import logging

from coalib.bears.LocalBear import LocalBear

class angularHtmlCheckBear(LocalBear):
    def run(self,
            filename,
            file):
            for line in file:
                if 'href=:'   in line:
                    logging.debug("Found URL!")
                    yield self.new_result("Found URL`s in CODE:" + line + ".", file=filename)
                else:
                    logging.debug("Checking line")
 		
