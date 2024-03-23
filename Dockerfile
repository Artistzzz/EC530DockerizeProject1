FROM python
WORKDIR /app
COPY . .
RUN pip install numpy

RUN pip install pytest
CMD ["pytest"]