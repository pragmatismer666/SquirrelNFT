This program follows the https://medium.com/scrappy-squirrels/tutorial-create-generative-nft-art-with-rarities-8ee6ce843133 tutorial to generate random NFTs by stacking PNG images on top of one another. 

Images were generated using rounakbanik's generative-art-nft library https://github.com/rounakbanik/generative-art-nft

metadata was already generated. This was then convereted into json format.

Goals 

1. Generate Squirrel image variations.
2. Build metadata for each squirrel variation and store it in json file. 
3. Upload squirrel images to IFPS node and retrieve tokenURI for each image. Store this information in another json file. 
4. Randomly assign a variation to the new nft. 
5. Create the token with the meta data.
6. Set Token URI

This program uses the Brownie Python based development and testing framework. https://eth-brownie.readthedocs.io/en/stable/

See https://testnets.opensea.io/assets/0x52f91FF55c971c422b6514Ae668aD81B5DC84e08/0 for an example of the NFT. 
