// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract SquirrelNFT is ERC721, VRFConsumerBase {
    uint256 public tokenCounter;
    bytes32 public keyhash;
    uint256 public fee;
    uint8 public tokenVariation = 4;
    mapping(uint256 => uint8) public tokenIdToVariation;
    mapping(bytes32 => address) public requestIdToSender;
    event assignVariation(uint256 tokenId, uint8 variation);
    event requestedNFT(bytes32 indexed requestId, address requester);

    constructor(
        address _vrfCoordinator,
        address _linkToken,
        bytes32 _keyhash,
        uint256 _fee
    )
        public
        VRFConsumerBase(_vrfCoordinator, _linkToken)
        ERC721("SSquirrel", "SSQL")
    {
        tokenCounter = 0;
        keyhash = _keyhash;
        fee = _fee;
    }

    /***************************************
     *           Create the NFT            *
     **************************************/
    function createSquirrel() public returns (bytes32) {
        /*********************************************************************************
         *  VRFConsumerBase function requestRandomness(bytes32 _keyHash, uint256 _fee)   *
         *  returns bytes32 _keyHash, uint256 vRFSeed                                    *
         ********************************************************************************/
        bytes32 requestId = requestRandomness(keyhash, fee);
        requestIdToSender[requestId] = msg.sender;
        emit requestedNFT(requestId, msg.sender);
    }

    /****************************************
     *      Randomly Generate Image         *
     *********************************************************************************
     *  Overriding fulfillRandomness function. Image variation has already been      *
     *  created. This function selects one of those variations.                      *
     ********************************************************************************/
    function fulfillRandomness(bytes32 requestId, uint256 randomNumber)
        internal
        override
    {
        uint8 variation = uint8(randomNumber % tokenVariation);
        uint256 newTokenId = tokenCounter;
        tokenIdToVariation[newTokenId] = variation;
        emit assignVariation(newTokenId, variation);
        address owner = requestIdToSender[requestId];
        _safeMint(owner, newTokenId); // ERC721.sol function _safeMint(address to, uint256 tokenId)
        tokenCounter = tokenCounter + 1;
    }

    /****************************************
     *           Set Token URI              *
     ***************************************/
    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId), // ERC721.sol function _isApprovedOrOwner(address spender, uint256 tokenId) return bool
            "ERC721: Caller is not Owner or Approved!"
        );
        _setTokenURI(tokenId, _tokenURI); // ERC721.sol function _setTokenURI(uint256 tokenId, string memory _tokenURI)
    }
}
