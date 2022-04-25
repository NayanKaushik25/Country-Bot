import discord
from discord.ext import commands
from webserver import keep_alive
import os

client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
  print("Bot is currently online!")



#Countries starting with A
@client.command
async def Afghanistan(ctx):
  embed=discord.Embed(title="Afghanistan",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Afghanistan, is a landlocked country located at the crossroads of Central and South Asia. Referred to as the Heart of Asia, it is bordered by Pakistan to the east and south, Iran to the west, Turkmenistan to the northwest, Uzbekistan to the north, Tajikistan to the northeast, and China to the northeast and east. Occupying 652,864 square kilometers (252,072 sq mi) of land, the country is predominately mountainous with plains in the north and the southwest, which are separated by the Hindu Kush mountain range. As of 2021, its population is 40.2 million, composed mostly of ethnic Pashtuns, Tajiks, Hazaras, and Uzbeks. Kabul is the country's largest city and serves as its capital.",inline=False)
  embed.add_field(name="Capital",value="Kabul",inline=False)
  embed.add_field(name="Flag",value="<:flag_af:967393753755172884>",inline=False)
  embed.add_field(name="Population",value="40.2 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$72.91 billion",inline=False)
  embed.add_field(name="Currency",value="Afghani",inline=False)
  embed.add_field(name="Time Zone",value="UTC +4:30",inline=False)
  embed.add_field(name="Dialing Code",value="+93",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Albania(ctx):
  embed=discord.Embed(title="Albania",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Albania, officially the Republic of Albania (Albanian: Republika e Shqipërisë), is a country in Southeastern Europe. It is located on the Adriatic and Ionian Seas within the Mediterranean Sea and shares land borders with Montenegro to the northwest, Kosovo to the northeast, North Macedonia to the east and Greece to the south. Tirana is its capital and largest city, followed by Durrës, Vlorë, and Shkodër.",inline=False)
  embed.add_field(name="Capital",value="Tirana",inline=False)
  embed.add_field(name="Flag",value="<:flag_al:967716155437486142>",inline=False)
  embed.add_field(name="Population",value="2.84 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$42.59 billion",inline=False)
  embed.add_field(name="Currency",value="Lek",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+355",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Algeria(ctx):
  embed=discord.Embed(title="Algeria",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Algeria, officially the People's Democratic Republic of Algeria, is a country in the Maghreb region of North Africa. The country is the largest country by total area in Africa and in the Arab world, and is bordered to the northeast by Tunisia; to the east by Libya; to the southeast by Niger; to the southwest by Mali, Mauritania, and Western Sahara; to the west by Morocco; and to the north by the Mediterranean Sea. It has a semi-arid geography, with most of the population living in the fertile north and the Sahara dominating the geography of the south. Algeria covers an area of 2,381,741 square kilometres (919,595 sq mi), making it the world's tenth largest nation by area, and the largest nation in Africa. With a population of 44 million, Algeria is the ninth-most populous country in Africa, and the 32nd-most populous country in the world. The capital and largest city is Algiers, located in the far north on the Mediterranean coast.",inline=False)
  embed.add_field(name="Capital",value="Algiers",inline=False)
  embed.add_field(name="Flag",value="<:flag_dz:967716837812994089>",inline=False)
  embed.add_field(name="Population",value="44.7 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$581.18 billion",inline=False)
  embed.add_field(name="Currency",value="Algerian dinar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1",inline=False)
  embed.add_field(name="Dialing Code",value="+213",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Andorra(ctx):
  embed=discord.Embed(title="Andorra",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Andorra, officially the Principality of Andorra, is a sovereign landlocked microstate on the Iberian Peninsula, in the eastern Pyrenees, bordered by France to the north and Spain to the south. Believed to have been created by Charlemagne, Andorra was ruled by the count of Urgell until 988, when it was transferred to the Roman Catholic Diocese of Urgell. The present principality was formed by a charter in 1278. It is headed by two co-princes: the Bishop of Urgell in Catalonia, Spain and the President of France. Its capital and largest city is Andorra la Vella.",inline=False)
  embed.add_field(name="Capital",value="Andorra la Vella",inline=False)
  embed.add_field(name="Flag",value="<:flag_ad:967717370443481171>",inline=False)
  embed.add_field(name="Population",value="79,535",inline=False)
  embed.add_field(name="GDP (nominal)",value="$3.23 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+376",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Angola(ctx):
  embed=discord.Embed(title="Angola",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Angola, officially the Republic of Angola is a country on the west coast of Southern Africa. It is the second-largest Lusophone (Portuguese-speaking) country in both total area and population (behind Brazil), and is the seventh-largest country in Africa. It is bordered by Namibia to the south, the DR Congo to the north, Zambia to the east, and the Atlantic Ocean to the west. Angola has an exclave province, the province of Cabinda, that borders the Republic of the Congo and the Democratic Republic of the Congo. The capital and most populated city is Luanda.",inline=False)
  embed.add_field(name="Capital",value="Luanda",inline=False)
  embed.add_field(name="Flag",value="<:flag_ao:967718237712310302>",inline=False)
  embed.add_field(name="Population",value="33 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$213 billion",inline=False)
  embed.add_field(name="Kwanza",value="Afghani",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1",inline=False)
  embed.add_field(name="Dialing Code",value="+244",inline=False)
  await ctx.send(embed=embed)


@client.command
async def AntiguaandBarbuda(ctx):
  embed=discord.Embed(title="Antigua and Barbuda",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Antigua and Barbuda is a sovereign island country in the West Indies in the Americas, lying between the Caribbean Sea and the Atlantic Ocean. It consists of two major islands, Antigua and Barbuda separated by around 40 km (25 mi), and smaller islands (including Great Bird, Green, Guiana, Long, Maiden, Prickly Pear, York Islands, Redonda). The permanent population number is about 97,120 (2019 est.), with 97% residing on Antigua. The capital and largest port and city is St. John's on Antigua, with Codrington being the largest town on Barbuda. Lying near each other, Antigua and Barbuda are in the middle of the Leeward Islands, part of the Lesser Antilles, roughly at 17°N of the equator.",inline=False)
  embed.add_field(name="Capital",value="St. John's",inline=False)
  embed.add_field(name="Flag",value="<:flag_ag:967719198715432980>",inline=False)
  embed.add_field(name="Population",value="99,337",inline=False)
  embed.add_field(name="GDP (PPP)",value="$2.73 billion",inline=False)
  embed.add_field(name="Currency",value="East Carribean dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -4",inline=False)
  embed.add_field(name="Dialing Code",value="+1-268",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Argentina(ctx):
  embed=discord.Embed(title="Argentina",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Argentina, officially known as the Argentine Republic is a country in the southern half of South America. Argentina covers an area of 2,780,400 sq km (1,073,500 sq mi), making it the largest Spanish-speaking nation in the world by area. It is the second-largest country in South America after Brazil, the fourth-largest country in the Americas, and the eighth-largest country in the world. It shares the bulk of the Southern Cone with Chile to the west, and is also bordered by Bolivia and Paraguay to the north, Brazil to the northeast, Uruguay and the South Atlantic Ocean to the east, and the Drake Passage to the south. Argentina is a federal state subdivided into twenty-three provinces, and one autonomous city, which is the federal capital and largest city of the nation, Buenos Aires",inline=False)
  embed.add_field(name="Capital",value="Buenos Aires",inline=False)
  embed.add_field(name="Flag",value="<:flag_ar:967719968554758144>",inline=False)
  embed.add_field(name="Population",value="45.6 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.049 trillion",inline=False)
  embed.add_field(name="Currency",value="Argentine peso",inline=False)
  embed.add_field(name="Time Zone",value="UTC -3",inline=False)
  embed.add_field(name="Dialing Code",value="+54",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Armenia(ctx):
  embed=discord.Embed(title="Armenia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Armenia, officially the Republic of Armenia, is a landlocked country located in the Armenian Highlands of Western Asia. It is a part of the Caucasus region; and is bordered by Turkey to the west, Georgia to the north, the Lachin corridor under a Russian peacekeeping force, and Azerbaijan to the east, and Iran and the Azerbaijani exclave of Nakhchivan to the south. Yerevan is the capital and largest city.",inline=False)
  embed.add_field(name="Capital",value="Yerevan",inline=False)
  embed.add_field(name="Flag",value="<:flag_am:967720783696764938>",inline=False)
  embed.add_field(name="Population",value="2.96 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$43.55 billion",inline=False)
  embed.add_field(name="Currency",value="Dram",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+374",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Australia(ctx):
  embed=discord.Embed(title="Australia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Australia, officially the Commonwealth of Australia, is a sovereign country comprising the mainland of the Australian continent, the island of Tasmania, and numerous smaller islands. With an area of 7,617,930 square kilometres (2,941,300 sq mi), Australia is the largest country by area in Oceania and the world's sixth-largest country. Australia is the oldest, flattest, and driest inhabited continent, with the least fertile soils. It is a megadiverse country, and its size gives it a wide variety of landscapes and climates, with deserts in the centre, tropical rainforests in the north-east, and mountain ranges in the south-east.",inline=False)
  embed.add_field(name="Capital",value="Canberra",inline=False)
  embed.add_field(name="Flag",value="<:flag_au:967722252139376690>",inline=False)
  embed.add_field(name="Population",value="25.98 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.6 trillion",inline=False)
  embed.add_field(name="Currency",value="Australian dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +8 to UTC +10",inline=False)
  embed.add_field(name="Dialing Code",value="+61",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Austria(ctx):
  embed=discord.Embed(title="Austria",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Austria, officially the Republic of Austria, is a country in the southern part of Central Europe. It is a federation of nine states, one of which is the capital Vienna, the largest city and state by population. The country is bordered by Germany to the northwest, the Czech Republic to the north, Slovakia to the northeast, Hungary to the east, Slovenia and Italy to the south, and Switzerland and Liechtenstein to the west. It occupies a landlocked area of 83,879 sq km (32,386 sq mi) and has a population of roughly 9 million people. ",inline=False)
  embed.add_field(name="Capital",value="Vienna",inline=False)
  embed.add_field(name="Flag",value="<:flag_at:967723024184926208>",inline=False)
  embed.add_field(name="Population",value="8.93 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$582.13 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+43",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Azerbaijan(ctx):
  embed=discord.Embed(title="Azerbaijan",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Azerbaijan, officially the Azerbaijan Republic or the Republic of Azerbaijan, is a transcontinental country located at the boundary of Eastern Europe and Western Asia. It is a part of the South Caucasus region, and is bounded by the Caspian Sea to the east, Russia (Republic of Dagestan) to the north, Georgia to the northwest, Armenia and Turkey to the west, and Iran to the south. Baku is the capital and largest city. ",inline=False)
  embed.add_field(name="Capital",value="Baku",inline=False)
  embed.add_field(name="Flag",value="<:flag_az:967724638459273247>",inline=False)
  embed.add_field(name="Population",value="10.13 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$189 billion",inline=False)
  embed.add_field(name="Currency",value="Manat",inline=False)
  embed.add_field(name="Time Zone",value="UTC +4",inline=False)
  embed.add_field(name="Dialing Code",value="+994",inline=False)
  await ctx.send(embed=embed)




#Countries starting with B
@client.command
async def Bahamas(ctx):
  embed=discord.Embed(title="Bahamas",color=discord.Colour.orange())
  embed.add_field(name="Basic Info",value="Bahamas, known officially as the Commonwealth of The Bahamas, is a sovereign country within the Lucayan Archipelago of the West Indies in the Atlantic. It takes up 97% of the Lucayan Archipelago's land area and is home to 88% of the archipelago's population. The archipelagic state consists of more than 3000 islands, cays, and islets in the Atlantic Ocean, and is located north of Cuba and northwest of the island of Hispaniola (split between Haiti and the Dominican Republic) and the Turks and Caicos Islands, southeast of the American state of Florida, and east of the Florida Keys. The capital is Nassau on the island of New Providence.",inline=False)
  embed.add_field(name="Capital",value="Baku",inline=False)
  embed.add_field(name="Flag",value="<:flag_bs:967727804114419792>",inline=False)
  embed.add_field(name="Population",value="400,516",inline=False)
  embed.add_field(name="GDP (PPP)",value="$12.61 billion",inline=False)
  embed.add_field(name="Currency",value="Bahamian dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -5 or UTC -4",inline=False)
  embed.add_field(name="Dialing Code",value="+1 242",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Bahrain(ctx):
  embed=discord.Embed(title="Bahrain",color=discord.Colour.orange())
  embed.add_field(name="Basic Info",value="Bahrain, officially the Kingdom of Bahrain, is an island country in Western Asia. It is situated on the Persian Gulf, and comprises a small archipelago made up of 50 natural islands and an additional 33 artificial islands, centered on Bahrain Island which makes up around 83 percent of the country's landmass. Bahrain is situated between Qatar and the northeastern coast of Saudi Arabia, to which it is connected by the King Fahd Causeway. According to the 2020 census, the country's population numbers 1,501,635, of which 712,362 are Bahraini nationals. Bahrain spans some 760 square kilometres (290 sq mi), and is the third-smallest nation in Asia after the Maldives and Singapore. The capital and largest city is Manama.",inline=False)
  embed.add_field(name="Capital",value="Manama",inline=False)
  embed.add_field(name="Flag",value="<:flag_bh:967729911211098152>",inline=False)
  embed.add_field(name="Population",value="1.56 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$78.76 billion",inline=False)
  embed.add_field(name="Currency",value="Bahraini dinar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+973",inline=False)
  await ctx.send(embed=embed)



@client.command
async def Bangladesh(ctx):
  embed=discord.Embed(title="Bangladesh",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Bangladesh, officially the People's Republic of Bangladesh, is a country in South Asia. It is the eighth-most populous country in the world, with a population exceeding 163 million people in an area of either 148,460 square kilometres (57,320 sq mi) or 147,570 square kilometres (56,980 sq mi), making it one of the most densely populated countries in the world. Bangladesh shares land borders with India to the west, north, and east, and Myanmar to the southeast; to the south it has a coastline along the Bay of Bengal. It is narrowly separated from Nepal and Bhutan by the Siliguri Corridor; and from China by 100 km of the Indian state of Sikkim in the north. Dhaka, the capital and largest city, is the nation's economic, political, and cultural hub. Chittagong, the largest seaport, is the second-largest city. The official language is Bengali, one of the most eastern branches of the Indo-European language family. ",inline=False)
  embed.add_field(name="Capital",value="Dhaka",inline=False)
  embed.add_field(name="Flag",value="<:flag_bd:967731067874312202>",inline=False)
  embed.add_field(name="Population",value="161.37 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.07 trillion",inline=False)
  embed.add_field(name="Currency",value="Taka",inline=False)
  embed.add_field(name="Time Zone",value="UTC +6",inline=False)
  embed.add_field(name="Dialing Code",value="+880",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Barbados(ctx):
  embed=discord.Embed(title="Barbados",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Barbados is an island country in the Lesser Antilles of the West Indies, in the Caribbean region of the Americas, and the most easterly of the Caribbean Islands. It occupies an area of 432 sq km (167 sq mi) and has a population of about 287,000 (2019 estimate). Its capital and largest city is Bridgetown.",inline=False)
  embed.add_field(name="Capital",value="Bridgetown",inline=False)
  embed.add_field(name="Flag",value="<:flag_bb:967732242770165760>",inline=False)
  embed.add_field(name="Population",value="287,025",inline=False)
  embed.add_field(name="GDP (PPP)",value="$5.39 billion",inline=False)
  embed.add_field(name="Currency",value="Barbadian dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -4",inline=False)
  embed.add_field(name="Dialing Code",value="+1-246",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Belarus(ctx):
  embed=discord.Embed(title="Belarus",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Belarus, officially the Republic of Belarus, is a landlocked country in Eastern Europe. It is bordered by Russia to the east and northeast, Ukraine to the south, Poland to the west, and Lithuania and Latvia to the northwest. Covering an area of 207,600 square kilometres (80,200 sq mi) and with a population of 9.3 million, Belarus is the 13th-largest and the 20th-most populous country in Europe. The country is administratively divided into seven regions. Minsk is the capital and largest city.",inline=False)
  embed.add_field(name="Capital",value="Minsk",inline=False)
  embed.add_field(name="Flag",value="<flag:by:967733614752202762>",inline=False)
  embed.add_field(name="Population",value="9.25 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$185.88 billion",inline=False)
  embed.add_field(name="Currency",value="Minsk",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+375",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Belgium(ctx):
  embed=discord.Embed(title="Belgium",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Belgium, officially the Kingdom of Belgium, is a country in Northwestern Europe. The country is bordered by the Netherlands to the north, Germany to the east, Luxembourg to the southeast, France to the southwest, and the North Sea to the northwest. It covers an area of 30,689 km2 (11,849 sq mi) and has a population of more than 11.5 million, making it the 22nd most densely populated country in the world and the 6th most densely populated country in Europe, with a density of 376 per square kilometre (970/sq mi). The capital and largest city is Brussels; other major cities are Antwerp, Ghent, Charleroi, Liège, Bruges, Namur, and Leuven.",inline=False)
  embed.add_field(name="Capital",value="Brussels",inline=False)
  embed.add_field(name="Flag",value="<:flag_be:967734369835958312>",inline=False)
  embed.add_field(name="Population",value="11.49 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$715.65 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+32",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Belize(ctx):
  embed=discord.Embed(title="Belize",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Belize is a Caribbean country on the northeastern coast of Central America. It borders Mexico to the north, the Caribbean Sea to the east, and Guatemala to the west and south. It has an area of 22,970 square kilometres (8,867 sq mi) and a population of 419,199 (2020). Its mainland is about 290 km (180 mi) long and 110 km (68 mi) wide. It has the lowest population and population density in Central America. Its population growth rate of 1.87% per year (2018 estimate) is the second-highest in the region and one of the highest in the Western Hemisphere. Its capital is Belmopan, and its largest city is Belize City. ",inline=False)
  embed.add_field(name="Capital",value="Belmopan",inline=False)
  embed.add_field(name="Flag",value="<:flag_bz:967734899631087657>",inline=False)
  embed.add_field(name="Population",value="419,199",inline=False)
  embed.add_field(name="GDP (PPP)",value="$3.48 billion",inline=False)
  embed.add_field(name="Currency",value="Belize dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -6",inline=False)
  embed.add_field(name="Dialing Code",value="+501",inline=False)
  await ctx.send(embed=embed)

@client.command
async def Benin(ctx):
  embed=discord.Embed(title="Benin",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Benin, officially the Republic of Benin (French: République du Bénin) and formerly known as Dahomey, is a country in West Africa. It is bordered by Togo to the west, Nigeria to the east, Burkina Faso to the north-west, and Niger to the north-east. The majority of its population lives on the small southern coastline of the Bight of Benin, part of the Gulf of Guinea in the northernmost tropical portion of the Atlantic Ocean. The capital of Benin is Porto-Novo, but the seat of government is in Cotonou, the country's largest city and economic capital. Benin covers an area of 114,763 square kilometres (44,310 sq mi) and its population in 2018 was estimated to be approximately 11.49 million. Benin is a tropical nation, highly dependent on agriculture, and is a large exporter of palm oil and cotton. Substantial employment and income arise from subsistence farming.",inline=False)
  embed.add_field(name="Capital",value="Baku",inline=False)
  embed.add_field(name="Flag",value="<:flag_az:967724638459273247>",inline=False)
  embed.add_field(name="Population",value="11.49 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$29.91 billion",inline=False)
  embed.add_field(name="Currency",value="West African CFA franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1",inline=False)
  embed.add_field(name="Dialing Code",value="+229",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Bhutan(ctx):
  embed=discord.Embed(title="Bhutan",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Bhutan is a landlocked country in the Eastern Himalayas, located between China and India. Bhutan is known as Druk Yul, or Land of the Thunder Dragon. Nepal and Bangladesh are located near Bhutan but do not share a land border. The country has a population of over 754,000 and territory of 38,394 square kilometers (14,824 sq mi) which ranks 133rd in terms of land area and 160th in population. Bhutan is a constitutional monarchy with Vajrayana Buddhism as the state religion.",inline=False)
  embed.add_field(name="Capital",value="Thimpu",inline=False)
  embed.add_field(name="Flag",value="<:flag_bt:967737172419575838>",inline=False)
  embed.add_field(name="Population",value="754,388",inline=False)
  embed.add_field(name="GDP (PPP)",value="$9.85 billion",inline=False)
  embed.add_field(name="Currency",value="Ngultrum",inline=False)
  embed.add_field(name="Time Zone",value="UTC +6",inline=False)
  embed.add_field(name="Dialing Code",value="+975",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Bolivia(ctx):
  embed=discord.Embed(title="Bolivia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Bolivia, officially the Plurinational State of Bolivia, is a landlocked country located in western-central South America. The constitutional capital is Sucre, while the seat of government and executive capital is La Paz. The largest city and principal industrial center is Santa Cruz de la Sierra, located on the Llanos Orientales (tropical lowlands), a mostly flat region in the east of the country.",inline=False)
  embed.add_field(name="Capital",value="La Paz",inline=False)
  embed.add_field(name="Flag",value="<:flag_bo:967738374880387092>",inline=False)
  embed.add_field(name="Population",value="11.42 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$89 billion",inline=False)
  embed.add_field(name="Currency",value="Boliviano",inline=False)
  embed.add_field(name="Time Zone",value="UTC -4",inline=False)
  embed.add_field(name="Dialing Code",value="+591",inline=False)
  await ctx.send(embed=embed)



@client.command
async def BosniaandHerzegovina(ctx):
  embed=discord.Embed(title="BosniaandHerzegovina",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Bosnia and Herzegovina is a country at the crossroads of south and southeast Europe, located in the Balkans. The capital and largest city is Sarajevo. Bosnia and Herzegovina borders Serbia to the east, Montenegro to the southeast, and Croatia to the north and southwest. It is not entirely landlocked; in the south it has a narrow coast on the Adriatic Sea within the Mediterranean, which is about 20 kilometres (12 miles) long and surrounds the town of Neum. Bosnia, which is the inland region of the country, has a moderate continental climate with hot summers and cold, snowy winters. In the central and eastern regions of the country, the geography is mountainous, in the northwest it is moderately hilly, and in the northeast it is predominantly flat. Herzegovina, which is the smaller, southern region of the country, has a Mediterranean climate and is mostly mountainous.",inline=False)
  embed.add_field(name="Capital",value="Sarajevo",inline=False)
  embed.add_field(name="Flag",value="<:flag_ba:967739575856406548>",inline=False)
  embed.add_field(name="Population",value="3.47 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$56.43 billion",inline=False)
  embed.add_field(name="Currency",value="Convertible mark",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+387",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Botswana(ctx):
  embed=discord.Embed(title="Botswana",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Botswana, officially the Republic of Botswana (Setswana: Lefatshe la Botswana [lɪˈfatsʰɪ la bʊˈtswana]); is a landlocked country in Southern Africa. Botswana is topographically flat, with up to 70 percent of its territory being the Kalahari Desert. It is bordered by South Africa to the south and southeast, Namibia to the west and north, and Zimbabwe to the north-east. It is connected to Zambia across the short Zambezi River border by the Kazungula Bridge.",inline=False)
  embed.add_field(name="Capital",value="Gaborone",inline=False)
  embed.add_field(name="Flag",value="<:flag_bw:967740413412790372>",inline=False)
  embed.add_field(name="Population",value="2.25 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$43.38 billion",inline=False)
  embed.add_field(name="Currency",value="Pula",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+267",inline=False)
  await ctx.send(embed=embed)

@client.command
async def Brazil(ctx):
  embed=discord.Embed(title="Brazil",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Brazil, officially the Federative Republic of Brazil (Portuguese: República Federativa do Brasil), is the largest country in both South America and Latin America. At 8.5 million square kilometers (3,300,000 sq mi) and with over 211 million people, Brazil is the world's fifth-largest country by area and the sixth most populous. Its capital is Brasília, and its most populous city is São Paulo also the most populous city in the Western Hemisphere. The federation is composed of the union of the 26 states and the Federal District. It is the largest country to have Portuguese as an official language and the only one in the Americas",inline=False)
  embed.add_field(name="Capital",value="Brasilia",inline=False)
  embed.add_field(name="Flag",value="<:flag_br:967740966133968976>",inline=False)
  embed.add_field(name="Population",value="212.68 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$3.58 trillion",inline=False)
  embed.add_field(name="Currency",value="Real",inline=False)
  embed.add_field(name="Time Zone",value="UTC -2 to UTC -5",inline=False)
  embed.add_field(name="Dialing Code",value="+55",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Brunei(ctx):
  embed=discord.Embed(title="Brunei",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Brunei, is a country located on the north coast of the island of Borneo in Southeast Asia. Apart from its South China Sea coast, it is completely surrounded by the Malaysian state of Sarawak. It is separated into two parts by the Sarawak district of Limbang. Brunei is the only sovereign state entirely on Borneo; the remainder of the island is divided between Malaysia and Indonesia. As of 2020, its population was 460,345, of whom about 100,000 live in the capital and largest city, Bandar Seri Begawan.",inline=False)
  embed.add_field(name="Capital",value="Bandar Seri Begawan",inline=False)
  embed.add_field(name="Flag",value="<:flag_bn:967743601956233216>",inline=False)
  embed.add_field(name="Population",value="460,345",inline=False)
  embed.add_field(name="GDP (PPP)",value="$33.38 billion",inline=False)
  embed.add_field(name="Currency",value="Brunei dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +8",inline=False)
  embed.add_field(name="Dialing Code",value="+673",inline=False)
  await ctx.send(embed=embed)


@client.command
async def Bulgaria(ctx):
  embed=discord.Embed(title="Bulgaria",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Bulgaria, officially the Republic of Bulgaria, is a country in Southeast Europe. It occupies the whole eastern part of the Balkans, and is bordered by Romania to the north, Serbia and North Macedonia to the west, Greece and Turkey to the south, and the Black Sea to the east. Bulgaria covers a territory of 110,994 square kilometres (42,855 sq mi), and is the sixteenth-largest country in Europe. Sofia is the nation's capital and largest city; other major cities are Plovdiv, Varna and Burgas.",inline=False)
  embed.add_field(name="Capital",value="Sofia",inline=False)
  embed.add_field(name="Flag",value="<flag_bg:967745163734687774>",inline=False)
  embed.add_field(name="Population",value="6.86 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$203 billion",inline=False)
  embed.add_field(name="Currency",value="Lev",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2 or UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+359",inline=False)
  await ctx.send(embed=embed)


@client.command
async def BurkinaFaso(ctx):
  embed=discord.Embed(title="Burkina Faso",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Burkina Faso, is a landlocked country in West Africa with an area of 274,200 square kilometres (105,900 sq mi), bordered by Mali to the northwest, Niger to the northeast, Benin to the southeast, Togo and Ghana to the south, and the Ivory Coast to the southwest. It has a population of 20,321,378. Previously called Republic of Upper Volta (1958–1984), it was renamed Burkina Faso by President Thomas Sankara. Its citizens are known as Burkinabè (/bɜːrˈkiːnəbeɪ/ bur-KEE-nə-bay), and its capital and largest city is Ouagadougou.",inline=False)
  embed.add_field(name="Capital",value="Ouagadougou",inline=False)
  embed.add_field(name="Flag",value="<flag_bf:967745737360306216>",inline=False)
  embed.add_field(name="Population",value="21.51 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$45.33 billion",inline=False)
  embed.add_field(name="Currency",value="West African CFA franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC",inline=False)
  embed.add_field(name="Dialing Code",value="+226",inline=False)
  await ctx.send(embed=embed)



@client.command
async def Burundi(ctx):
  embed=discord.Embed(title="Burundi",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Burundi, officially the Republic of Burundi is a landlocked country in the Great Rift Valley where the African Great Lakes region and East Africa converge. It is bordered by Rwanda to the north, Tanzania to the east and southeast, and the Democratic Republic of the Congo to the west; Lake Tanganyika lies along its southwestern border. The capital cities are Gitega and Bujumbura, the latter of which is the country's largest city.",inline=False)
  embed.add_field(name="Capital",value="Gitega",inline=False)
  embed.add_field(name="Flag",value="<flag:bi:967746359987937350>",inline=False)
  embed.add_field(name="Population",value="11.86 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$8.38 billion",inline=False)
  embed.add_field(name="Currency",value="Burundian franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+257",inline=False)
  await ctx.send(embed=embed)

  
  
  
#Countries Staring with C
@client.command()
async def CaboVerde(ctx):
  embed=discord.Embed(title="Cabo Verde",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Cabo Verde, officially the Republic of Cabo Verde, is an archipelago and island country in the central Atlantic Ocean, consisting of ten volcanic islands with a combined land area of about 4,033 square kilometres (1,557 sq mi). These islands lie between 600 to 850 kilometres (320 to 460 nautical miles) west of Cap-Vert, the westernmost point of continental Africa. The Cape Verde islands form part of the Macaronesia ecoregion, along with the Azores, the Canary Islands, Madeira, and the Savage Isles. ",inline=False)
  embed.add_field(name="Capital",value="Praia",inline=False)
  embed.add_field(name="Flag",value="<:flag_cv:968088541177470996>",inline=False)
  embed.add_field(name="Population",value="483,628",inline=False)
  embed.add_field(name="GDP (PPP)",value="$4.32 billion",inline=False)
  embed.add_field(name="Currency",value="Cape Verdean escudo",inline=False)
  embed.add_field(name="Time Zone",value="UTC -1",inline=False)
  embed.add_field(name="Dialing Code",value="+238",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Cambodia(ctx):
  embed=discord.Embed(title="Cambodia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Cambodia, officially the Kingdom of Cambodia, is a country located in the southern portion of the Indochinese Peninsula in Southeast Asia. It is 181,035 square kilometres (69,898 square miles) in area, bordering Thailand to the northwest, Laos to the north, Vietnam to the east, and the Gulf of Thailand to the southwest. The nation's capital and largest city is Phnom Penh.",inline=False)
  embed.add_field(name="Capital",value="Phnom Penh",inline=False)
  embed.add_field(name="Flag",value="<:flag_kh:968089919601905734>",inline=False)
  embed.add_field(name="Population",value="15.5 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$76.63 billion",inline=False)
  embed.add_field(name="Currency",value="Riel",inline=False)
  embed.add_field(name="Time Zone",value="UTC +7",inline=False)
  embed.add_field(name="Dialing Code",value="+855",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Cameroon(ctx):
  embed=discord.Embed(title="Cameroon",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Cameroon, officially the Republic of Cameroon (French: République du Cameroun), is a country in west-central Africa. It is bordered by Nigeria to the west and north; Chad to the northeast; the Central African Republic to the east; and Equatorial Guinea, Gabon and the Republic of the Congo to the south. Its coastline lies on the Bight of Biafra, part of the Gulf of Guinea and the Atlantic Ocean. The country is sometimes identified as West African and other times as Central African, due to its strategic position at the crossroads between West and Central Africa. Its nearly 25 million people speak 250 native languages.",inline=False)
  embed.add_field(name="Capital",value="Yaounde",inline=False)
  embed.add_field(name="Flag",value="<:flag_cm:968090559031939112>",inline=False)
  embed.add_field(name="Population",value="26.54 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$101.95 billion",inline=False)
  embed.add_field(name="Currency",value="Central African CFA franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1",inline=False)
  embed.add_field(name="Dialing Code",value="+237",inline=False)
  await ctx.send(embed=embed)




@client.command()
async def Canada(ctx):
  embed=discord.Embed(title="Canada",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Canada is a country in North America. Its ten provinces and three territories extend from the Atlantic Ocean to the Pacific Ocean and northward into the Arctic Ocean, covering 9.98 million square kilometres (3.85 million square miles), making it the world's second-largest country by total area. Its southern and western border with the United States, stretching 8,891 kilometres (5,525 mi), is the world's longest bi-national land border. Canada's capital is Ottawa, and its three largest metropolitan areas are Toronto, Montreal, and Vancouver.",inline=False)
  embed.add_field(name="Capital",value="Ottowa",inline=False)
  embed.add_field(name="Flag",value="<:flag_ca:968091151699673118>",inline=False)
  embed.add_field(name="Population",value="38.52 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$2.23 trillion",inline=False)
  embed.add_field(name="Currency",value="Canadian dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -3.5 to UTC -8",inline=False)
  embed.add_field(name="Dialing Code",value="+1",inline=False)
  await ctx.send(embed=embed)





@client.command()
async def CentralAfricanRepublic(ctx):
  embed=discord.Embed(title="Central African Republic",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="The Central African Republic is a landlocked country in Central Africa. It is bordered by Chad to the north, Sudan to the northeast, South Sudan to the southeast, the DR Congo to the south, the Republic of the Congo to the southwest, and Cameroon to the west.",inline=False)
  embed.add_field(name="Capital",value="Bangui",inline=False)
  embed.add_field(name="Flag",value="<:flag_cf:968092021006958612>",inline=False)
  embed.add_field(name="Population",value="4.66 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$4.26 billion",inline=False)
  embed.add_field(name="Currency",value="Bitcoin",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1",inline=False)
  embed.add_field(name="Dialing Code",value="+236",inline=False)
  await ctx.send(embed=embed)




@client.command()
async def Chad(ctx):
  embed=discord.Embed(title="Chad",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Chad, officially known as the Republic of Chad, is a landlocked country at the crossroads of North and Central Africa. It is bordered by Libya to the north, Sudan to the east, the Central African Republic to the south, Cameroon to the south-west, Nigeria to the southwest (at Lake Chad), and Niger to the west. Chad has a population of 16 million, of which 1.6 million live in the capital and largest city N'Djamena",inline=False)
  embed.add_field(name="Capital",value="N'Djamena",inline=False)
  embed.add_field(name="Flag",value="<:flag_td:968092563624063046>",inline=False)
  embed.add_field(name="Population",value="16.24 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$30 billion",inline=False)
  embed.add_field(name="Currency",value="Central African CFA franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1",inline=False)
  embed.add_field(name="Dialing Code",value="+235",inline=False)
  await ctx.send(embed=embed)




keep_alive()
TOKEN=os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
