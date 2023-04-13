FROM debian
RUN apt-get update
RUN apt-get install -y procps curl nginx
COPY start.sh /
RUN chmod +x /start.sh
EXPOSE 80
CMD [ "/start.sh" ]
