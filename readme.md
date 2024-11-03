# NFT Charity Auction

The charity NFT auction is a decentralized application aimed at raising funds for various needs. Anyone who joins the fundraising effort and contributes a minimum amount automatically participates in the auction and has a chance to win unique NFTs. The project is built on Django for the backend and integrated with the Ethereum blockchain, utilizing smart contracts.
## Features

- **Create and Manage Auctions**: Users can create auctions for NFTs and set goals for charity.
- **Smart Contracts**: Secure, transparent transactions using Ethereum smart contracts.
- **Admin Panel**: Manage NFT metadata, auction details, and network transactions.

## Technologies

- **Backend**: Django, Django Rest Framework, Celery
- **Blockchain**: Solidity smart contracts, Web3.py
- **Database**: PostgreSQL
- **Server**: Nginx
- **Containers**: Docker, Docker Compose 
- **Caching and Task Queue**: Redis

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/g1Den1s-it/NFTCharityAuction.git

2. Run Docker 
   ```bash
   docker-compose up --build -d 
