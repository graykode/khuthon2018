# JustKode는 뭘 했나요?
저는 음식 리뷰 사이트의 Crawling과 AWS lambda 함수를 통한 DynamoDB 쿼리 질의를 구현했습니다!

<p align="center"><img width="100" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png">
<img width="100" src="https://cdn-images-1.medium.com/max/1200/1*foHs8AleRqNMimdXsK9hAA.png">
<img width="100" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/DynamoDB.png/220px-DynamoDB.png"></p>

## 검색 우선순위는 어떻게 구현하였나요?
CNN을 통한 평점 평균에 가중치 2, 리뷰 갯수에 따라 가중치 3을 주어 그 가중치의 합을 통해 내림차순으로 정렬 하였습니다.

## 코드는...
보안상의 이유로 크롤링 코드, lambda 함수 코드를 없앴습니다.

## Crawling에 사용한 패키지
- BeautifulSoup
- Requests

## Lambda에 사용한 node 모듈
- AWS-sdk
