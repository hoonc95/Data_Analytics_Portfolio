{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red103\green107\blue114;\red0\green0\blue0;\red195\green123\blue90;
\red174\green176\blue183;\red160\green0\blue163;\red128\green63\blue122;\red89\green158\blue96;\red71\green149\blue242;
\red164\green160\blue78;\red38\green157\blue169;\red117\green114\blue185;}
{\*\expandedcolortbl;;\csgenericrgb\c40392\c41961\c44706;\csgray\c0\c0;\csgenericrgb\c76471\c48235\c35294;
\csgenericrgb\c68235\c69020\c71765;\csgenericrgb\c62745\c0\c63922;\csgenericrgb\c50196\c24706\c47843;\csgenericrgb\c34902\c61961\c37647;\csgenericrgb\c27843\c58431\c94902;
\csgenericrgb\c64314\c62745\c30588;\csgenericrgb\c14902\c61569\c66275;\csgenericrgb\c45882\c44706\c72549;}
\paperw11900\paperh16840\margl1440\margr1440\vieww17820\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs26 \cf2 \cb3 # IMPORT LIBRARY\
\cf4 import \cf5 hashlib\
\
\
\cf2 # CREATE TRANSACTION CLASS\
\cf4 class \cf5 Transaction:\
    \cf4 def \cf6 __init__\cf5 (\cf7 self\cf5 , sender, receiver, amount):\
        \cf7 self\cf5 .sender = sender\
        \cf7 self\cf5 .receiver = receiver\
        \cf7 self\cf5 .amount = amount\
\
    \cf4 def \cf6 __str__\cf5 (\cf7 self\cf5 ):\
        \cf4 return \cf8 f"\cf4 \{\cf7 self\cf5 .sender\cf4 \}\cf8  -> \cf4 \{\cf7 self\cf5 .receiver\cf4 \}\cf8 : \cf4 \{\cf7 self\cf5 .amount\cf4 \}\cf8 "\
\
\
\cf2 # CREATE BLOCK CLASS\
\cf4 class \cf5 Block:\
    \cf4 def \cf6 __init__\cf5 (\cf7 self\cf5 , data, prev_hash):\
        \cf7 self\cf5 .data = data\
        \cf7 self\cf5 .prev_hash = prev_hash\
        \cf7 self\cf5 .hash = \cf7 self\cf5 .calc_hash()\
\
    \cf4 def \cf9 calc_hash\cf5 (\cf7 self\cf5 ):\
        sha = hashlib.sha256()\
        sha.update(\cf7 self\cf5 .data.encode(\cf8 'utf-8'\cf5 ))\
        \cf4 return \cf5 sha.hexdigest()\
\
\
\cf2 # CREATE BLOCKCHAIN CLASS\
\cf4 class \cf5 Blockchain:\
    \cf4 def \cf6 __init__\cf5 (\cf7 self\cf5 ):\
        \cf7 self\cf5 .chain = [\cf7 self\cf5 .create_genesis_block()]\
        \cf7 self\cf5 .balances = \{\}\
\
    \cf10 @staticmethod\
    \cf4 def \cf9 create_genesis_block\cf5 ():\
        \cf4 return \cf5 Block(\cf8 "Genesis Block"\cf5 , \cf8 "0"\cf5 )\
\
    \cf4 def \cf9 add_block\cf5 (\cf7 self\cf5 , data):\
        prev_block = \cf7 self\cf5 .chain[-\cf11 1\cf5 ]\
        new_block = Block(data, prev_block.hash)\
        \cf7 self\cf5 .chain.append(new_block)\
\
    \cf4 def \cf9 add_transaction\cf5 (\cf7 self\cf5 , transaction):\
        \cf2 # UPDATE BALANCES\
        \cf5 sender, receiver, amount = transaction.sender, transaction.receiver, transaction.amount\
        \cf2 # SKIP BALANCE UPDATE for the GENESIS BLOCK\
        \cf4 if \cf5 sender != \cf8 "Genesis Block"\cf5 :\
            \cf7 self\cf5 .balances[sender] = \cf7 self\cf5 .balances.get(sender, \cf11 0\cf5 ) - amount\
            \cf7 self\cf5 .balances[receiver] = \cf7 self\cf5 .balances.get(receiver, \cf11 0\cf5 ) + amount\
\
        \cf2 # ADD TRANSACTION as a BLOCK\
        \cf7 self\cf5 .add_block(\cf12 str\cf5 (transaction))\
\
    \cf4 def \cf9 print_blockchain_with_balances\cf5 (\cf7 self\cf5 ):\
        \cf12 print\cf5 (\cf8 'Blockchain:'\cf5 )\
        \cf4 for \cf5 block \cf4 in \cf7 self\cf5 .chain:\
            \cf12 print\cf5 (\cf8 'Data:'\cf5 , block.data)\
            \cf12 print\cf5 (\cf8 'Previous Hash:'\cf5 , block.prev_hash)\
            \cf12 print\cf5 (\cf8 'Hash:'\cf5 , block.hash)\
\
            \cf2 # PRINT BALANCES of TRANSACTIONAL PARTIES\
            \cf4 if \cf8 "->" \cf4 in \cf5 block.data:\
                parties = block.data.split(\cf8 " -> "\cf5 )\
                sender = parties[\cf11 0\cf5 ]\
                receiver = parties[\cf11 1\cf5 ].split(\cf8 ":"\cf5 )[\cf11 0\cf5 ]\
                \cf12 print\cf5 (\cf8 f"Balance| \cf4 \{\cf5 sender\cf4 \}\cf8 : \cf4 \{\cf7 self\cf5 .balances.get(sender, \cf11 0\cf5 )\cf4 \}\cf8 "\cf5 )\
                \cf12 print\cf5 (\cf8 f"Balance| \cf4 \{\cf5 receiver\cf4 \}\cf8 : \cf4 \{\cf7 self\cf5 .balances.get(receiver, \cf11 0\cf5 )\cf4 \}\cf8 "\cf5 )\
            \cf12 print\cf5 ()\
\
\
\cf2 # TEST BLOCKCHAIN\
\cf5 blockchain = Blockchain()\
\
\cf2 # ADD TRANSACTIONS to the BLOCKCHAIN\
\cf5 blockchain.add_transaction(Transaction(\cf8 "Genesis Block"\cf5 , \cf8 "Alice"\cf5 , \cf11 100\cf5 ))\
blockchain.add_transaction(Transaction(\cf8 "Alice"\cf5 , \cf8 "Bob"\cf5 , \cf11 50\cf5 ))\
blockchain.add_transaction(Transaction(\cf8 "Bob"\cf5 , \cf8 "Charlie"\cf5 , \cf11 30\cf5 ))\
blockchain.add_transaction(Transaction(\cf8 "Charlie"\cf5 , \cf8 "Dave"\cf5 , \cf11 20\cf5 ))\
\
\cf2 # PRINT BLOCKCHAIN w/ BALANCES of TRANSACTIONAL PARTIES\
\cf5 blockchain.print_blockchain_with_balances()\
\
}