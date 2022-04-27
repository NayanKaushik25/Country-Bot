import discord
from discord.ext import commands
from webserver import keep_alive
import os

client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
  print("Bot is currently online!")



#Countries starting with A
@client.command()
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


@client.command()
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


@client.command()
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


@client.command()
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


@client.command()
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


@client.command()
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


@client.command()
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


@client.command()
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


@client.command()
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


@client.command()
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


@client.command()
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
@client.command()
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


@client.command()
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



@client.command()
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


@client.command()
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


@client.command()
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


@client.command()
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


@client.command()
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

@client.command()
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


@client.command()
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


@client.command()
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



@client.command()
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


@client.command()
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

@client.command()
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


@client.command()
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


@client.command()
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


@client.command()
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



@client.command()
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
  embed.add_field(name="Capital",value="Ottawa",inline=False)
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


  
@client.command()
async def Chile(ctx):
  embed=discord.Embed(title="Chile",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Chile, officially the Republic of Chile, is a country in the western part of South America. It occupies a long, narrow strip of land between the Andes to the east and the Pacific Ocean to the west. Chile covers an area of 756,096 square kilometers (291,930 sq mi), with a population of 17.5 million as of 2017. Chile is the southernmost country in the world, the closest to Antarctica, and shares land borders with Peru to the north, Bolivia to the north-east, Argentina to the east, and the Drake Passage in the far south. Chile also controls the Pacific islands of Juan Fernández, Isla Salas y Gómez, Desventuradas, and Easter Island in Oceania. It also claims about 1,250,000 square kilometers (480,000 sq mi) of Antarctica under the Chilean Antarctic Territory. The country's capital and largest city is Santiago, and its national language is Spanish.",inline=False)
  embed.add_field(name="Capital",value="Santiago",inline=False)
  embed.add_field(name="Flag",value="<:flag_cl:968423042852196352>",inline=False)
  embed.add_field(name="Population",value="17.57 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$550.45 billion",inline=False)
  embed.add_field(name="Currency",value="Chilean peso",inline=False)
  embed.add_field(name="Time Zone",value="UTC -4 to UTC -6",inline=False)
  embed.add_field(name="Dialing Code",value="+56",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def China(ctx):
  embed=discord.Embed(title="China",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="China (Chinese: 中国; pinyin: Zhōngguó), officially the People's Republic of China (PRC; Chinese: 中华人民共和国; pinyin: Zhōnghuá Rénmín Gònghéguó), is a country in East Asia. It is the world's most populous country, with a population of more than 1.4 billion. China spans five geographical time zones and borders 14 countries, the second most of any country in the world after Russia. Covering an area of approximately 9.6 million square kilometers (3,700,000 sq mi), it is the world's third or fourth largest country. The country consists of 23 provinces, five autonomous regions, four municipalities, and two Special Administrative Regions (Hong Kong and Macau). The national capital is Beijing and the largest city is Shanghai.",inline=False)
  embed.add_field(name="Capital",value="Beijing",inline=False)
  embed.add_field(name="Flag",value="<:flag_cn:968424046549155850>",inline=False)
  embed.add_field(name="Population",value="1.41 billion",inline=False)
  embed.add_field(name="GDP (PPP)",value="$30.18 trillion",inline=False)
  embed.add_field(name="Currency",value="Renminbi",inline=False)
  embed.add_field(name="Time Zone",value="UTC +8",inline=False)
  embed.add_field(name="Dialing Code",value="+86 (Mainland), +852 (Hong Kong) and +853 (Macau)",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Colombia(ctx):
  embed=discord.Embed(title="Colombia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Colombia, officially the Republic of Colombia, is a transcontinental country spanning South America and an insular region in North America. It is bordered by the Caribbean Sea to the north, Venezuela to the east, Brazil to the southeast, Ecuador and Peru to the south, the Pacific Ocean to the west, and Panama to the northwest. Colombia comprises 32 departments and the Capital District of Bogotá, the country's largest city. It covers an area of 1,141,748 square kilometers (440,831 sq mi), with a population of 50 million. Colombia's rich cultural heritage reflects influences by various Amerindian civilizations, European settlement, African slaves, and immigration from Europe and the Middle East. Spanish is the nation's official language, besides which over 70 languages are spoken.",inline=False)
  embed.add_field(name="Capital",value="Bogota",inline=False)
  embed.add_field(name="Flag",value="<:flag_co:968425177585172520>",inline=False)
  embed.add_field(name="Population",value="50.37 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$940.58 billion",inline=False)
  embed.add_field(name="Currency",value="Colombian peso",inline=False)
  embed.add_field(name="Time Zone",value="UTC -5",inline=False)
  embed.add_field(name="Dialing Code",value="+57",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Comoros(ctx):
  embed=discord.Embed(title="Comoros",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="The Comoros, officially the Union of the Comoros, is an archipelagic country in the Indian Ocean, at the northern end of the Mozambique Channel off the eastern coast of Africa. It shares maritime borders with Madagascar and Mayotte to the southeast, Tanzania to the northwest, Mozambique to the west, and the Seychelles to the northeast. Its capital and largest city is Moroni. The religion of the majority of the population, and the official state religion, is Sunni Islam. As a member of the Arab League, it is the only country in the Arab world which is entirely in the Southern Hemisphere. It is also a member state of the African Union, the Organisation internationale de la Francophonie, the Organisation of Islamic Cooperation, and the Indian Ocean Commission. The country has three official languages: Comorian, French and Arabic.",inline=False)
  embed.add_field(name="Capital",value="Moroni",inline=False)
  embed.add_field(name="Flag",value="<:flag_km:968425972728750080>",inline=False)
  embed.add_field(name="Population",value="850,866",inline=False)
  embed.add_field(name="GDP (PPP)",value="$2.44 billion",inline=False)
  embed.add_field(name="Currency",value="Comorian franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+269",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Congo(ctx):
  embed=discord.Embed(title="The Republic of Congo",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="The Republic of Congo, also known as Congo-Brazzaville, the Congo Republic or simply either Congo or the Congo, is a country located in the western coast of Central Africa. The country is bordered to the west by Gabon, to its northwest by Cameroon and its northeast by the Central African Republic, to the southeast by the DR Congo, to its south by the Angolan exclave of Cabinda and to its southwest by the Atlantic Ocean. French is the official language of the Republic of the Congo. ",inline=False)
  embed.add_field(name="Capital",value="Brazaville",inline=False)
  embed.add_field(name="Flag",value="<:flag_cg:968426887829418004>",inline=False)
  embed.add_field(name="Population",value="5.65 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$25.89 billion",inline=False)
  embed.add_field(name="Currency",value="Central African CFA franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1",inline=False)
  embed.add_field(name="Dialing Code",value="+242",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def CostaRica(ctx):
  embed=discord.Embed(title="Costa Rica",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Costa Rica, officially the Republic of Costa Rica (Spanish: República de Costa Rica), is a country in Central America, bordered by Nicaragua to the north, the Caribbean Sea to the northeast, Panama to the southeast, the Pacific Ocean to the southwest, and maritime border with Ecuador to the south of Cocos Island. It has a population of around five million[10][11] in a land area of 51,060 km2 (19,710 sq mi). An estimated 333,980 people live in the capital and largest city, San José, with around two million people in the surrounding metropolitan area.",inline=False)
  embed.add_field(name="Capital",value="San Jose",inline=False)
  embed.add_field(name="Flag",value="<:flag_cr:968427580954931210>",inline=False)
  embed.add_field(name="Population",value="5.09 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$95.79 billion",inline=False)
  embed.add_field(name="Currency",value="Costa Rican colon",inline=False)
  embed.add_field(name="Time Zone",value="UTC -6",inline=False)
  embed.add_field(name="Dialing Code",value="+506",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def IvoryCoast(ctx):
  embed=discord.Embed(title="Ivory Coast",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Ivory Coast, also known as Côte d'Ivoire, officially the Republic of Côte d'Ivoire, is a country on the southern coast of West Africa. Its political capital is Yamoussoukro, in the centre of the country; while its largest city and economic centre is the port city of Abidjan. It borders Guinea to the northwest, Liberia to the west, Mali to the northwest, Burkina Faso to the northeast, Ghana to the east, and the Gulf of Guinea (Atlantic Ocean) to the south. Its official language is French, and indigenous languages are also widely used, including Bété, Baoulé, Dioula, Dan, Anyin, and Cebaara Senufo. In total, there are around 78 different languages spoken in Ivory Coast. The country has a religiously diverse population, including numerous followers of Christianity, Islam, and indigenous faiths.",inline=False)
  embed.add_field(name="Capital",value="Yamoussourko",inline=False)
  embed.add_field(name="Flag",value="<:flag_ci:968428380494131200>",inline=False)
  embed.add_field(name="Population",value="26.37 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$173.18 billion",inline=False)
  embed.add_field(name="Currency",value="West African CFA franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC",inline=False)
  embed.add_field(name="Dialing Code",value="+225",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Croatia(ctx):
  embed=discord.Embed(title="Croatia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Croatia, officially the Republic of Croatia (Croatian: Republika Hrvatska, is a country at the crossroads of Central and Southeast Europe. It shares a coastline along the Adriatic Sea, and borders Slovenia to the northwest, Hungary to the northeast, Serbia to the east, Bosnia and Herzegovina and Montenegro to the southeast, and shares a maritime border with Italy to the west and southwest. Croatia's capital and largest city, Zagreb, forms one of the country's primary subdivisions, with twenty counties. The country spans an area of 56,594 square kilometres (21,851 square miles), with a population of nearly 3.9 million.",inline=False)
  embed.add_field(name="Capital",value="Zagreb",inline=False)
  embed.add_field(name="Flag",value="<:flag_hr:968428824343748618>",inline=False)
  embed.add_field(name="Population",value="3.88 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$145 billion",inline=False)
  embed.add_field(name="Currency",value="Croatian kuna",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+385",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Cuba(ctx):
  embed=discord.Embed(title="Cuba",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Cuba, is a country comprising the island of Cuba, as well as Isla de la Juventud and several minor archipelagos. Cuba is located where the northern Caribbean Sea, Gulf of Mexico, and Atlantic Ocean meet. Cuba is located at the east of the Yucatán Peninsula (Mexico), south of both the American state of Florida and the Bahamas, west of Hispaniola (Haiti/Dominican Republic), and north of both Jamaica and the Cayman Islands. Havana is the largest city and capital; other major cities include Santiago de Cuba and Camagüey. The official area of the Republic of Cuba is 109,884 km2 (42,426 sq mi) (without the territorial waters). The main island of Cuba is the largest island in Cuba and in the Caribbean, with an area of 104,556 sq km (40,369 sq mi). Cuba is the second-most populous country in the Caribbean after Haiti, with over 11 million inhabitants.",inline=False)
  embed.add_field(name="Capital",value="Havana",inline=False)
  embed.add_field(name="Flag",value="<:flag_cu:968429815973691392>",inline=False)
  embed.add_field(name="Population",value="11.18 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$254.86 billion",inline=False)
  embed.add_field(name="Currency",value="Cuban peso",inline=False)
  embed.add_field(name="Time Zone",value="UTC -5 or UTC -4",inline=False)
  embed.add_field(name="Dialing Code",value="+53",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Cyprus(ctx):
  embed=discord.Embed(title="Cuba",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Cyprus, officially the Republic of Cyprus, is an island country in the eastern Mediterranean Sea south of the Anatolian Peninsula. It is the third-largest and third-most populous island in the Mediterranean, and is south of Turkey and west of Syria. Its capital and largest city is Nicosia.",inline=False)
  embed.add_field(name="Capital",value="Nicosia",inline=False)
  embed.add_field(name="Flag",value="<:flag_cy:968430926197559306>",inline=False)
  embed.add_field(name="Population",value="1.18 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$43.8 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2 or UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+357",inline=False)
  await ctx.send(embed=embed)

@client.command()
async def CzechRepublic(ctx):
  embed=discord.Embed(title="Czech Republic",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="The Czech Republic also called Czechia, is a landlocked country in Central Europe. Historically known as Bohemia, it is bordered by Austria to the south, Germany to the west, Poland to the northeast, and Slovakia to the southeast. The Czech Republic has a hilly landscape that covers an area of 78,871 square kilometers (30,452 sq mi) with a mostly temperate continental and oceanic climate. The capital and largest city is Prague; other major cities and urban areas include Brno, Ostrava, Plzeň and Liberec.",inline=False)
  embed.add_field(name="Capital",value="Prague",inline=False)
  embed.add_field(name="Flag",value="<:flag_cz:968431912634961940>",inline=False)
  embed.add_field(name="Population",value="10.7 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$509.95 billion",inline=False)
  embed.add_field(name="Currency",value="Czech koruna",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+420",inline=False)
  await ctx.send(embed=embed)


#Countries starting with D
@client.command()
async def NorthKorea(ctx):
  embed=discord.Embed(title="North Korea",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="North Korea, officially the Democratic People's Republic of Korea (DPRK), is a country in East Asia. It constitutes the northern half of the Korean Peninsula and shares borders with China and Russia to the north, at the Yalu (Amnok) and Tumen rivers, and South Korea to the south at the Korean Demilitarized Zone. The country's western border is formed by the Yellow Sea, while its eastern border is defined by the Sea of Japan. North Korea, like its southern counterpart, claims to be the legitimate government of the entire peninsula and adjacent islands. Pyongyang is the capital and largest city. ",inline=False)
  embed.add_field(name="Capital",value="Pyongyang",inline=False)
  embed.add_field(name="Flag",value="<:flag_kp:968433735370412052>",inline=False)
  embed.add_field(name="Population",value="25.54 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$40 billion",inline=False)
  embed.add_field(name="Currency",value="Korean People's won",inline=False)
  embed.add_field(name="Time Zone",value="UTC +9",inline=False)
  embed.add_field(name="Dialing Code",value="+850",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def DRC(ctx):
  embed=discord.Embed(title="Democratic Republic of the Congo",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="The Democratic Republic of the Congo, informally Congo-Kinshasa, DR Congo, the DRC, the DROC, or the Congo, and formerly and also colloquially Zaire, is a country in Central Africa. It is, by area, the second largest country in Africa (after Algeria), and the 11th-largest in the world. With a population of around 92 million, the Democratic Republic of the Congo is the most populous officially Francophone country in the world. It is a member of the United Nations, Non-Aligned Movement, African Union, COMESA, and the East African Community. The capital and largest city is Kinshasa, which is also the world's most populous Francophone city. ",inline=False)
  embed.add_field(name="Capital",value="Kinshasa",inline=False)
  embed.add_field(name="Flag",value="<:flag_cd:968434268722315274>",inline=False)
  embed.add_field(name="Population",value="92.37 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$121.56 billion",inline=False)
  embed.add_field(name="Currency",value="Congolese franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 to UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+243",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Denmark(ctx):
  embed=discord.Embed(title="Denmark",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Denmark, is a Nordic country in Northern Europe. It is the most populous and politically central constituent of the Kingdom of Denmark, a constitutionally unitary state that includes the autonomous territories of the Faroe Islands and Greenland in the North Atlantic Ocean. European Denmark is the southernmost of the Scandinavian countries, lying southwest of Sweden, south of Norway,[N 14] and north of Germany.",inline=False)
  embed.add_field(name="Capital",value="Copenhagen",inline=False)
  embed.add_field(name="Flag",value="<:flag_dk:968442712577695754>",inline=False)
  embed.add_field(name="Population",value="5.87 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$391.90 billion",inline=False)
  embed.add_field(name="Currency",value="Danish krone",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 to UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+45 (Denmark), +298 (Faroe Islands) and +299 (Greenland)",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Djibouti(ctx):
  embed=discord.Embed(title="Djibouti",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Djibouti, officially the Republic of Djibouti, is a country located in the Horn of Africa. It is bordered by Somalia in the south, Ethiopia in the southwest, Eritrea in the north, and the Red Sea and the Gulf of Aden in the east. Across the Gulf of Aden is Yemen. The country has a total area of 23,200 sq km (8,958 sq mi)",inline=False)
  embed.add_field(name="Capital",value="Djibouti",inline=False)
  embed.add_field(name="Flag",value="<:flag_dj:968444092893777991>",inline=False)
  embed.add_field(name="Population",value="921,804",inline=False)
  embed.add_field(name="GDP (PPP)",value="$3.97 billion",inline=False)
  embed.add_field(name="Currency",value="Djiboutian franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+253",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Dominica(ctx):
  embed=discord.Embed(title="Dominica",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Dominica, officially the Commonwealth of Dominica, is an island country in the Caribbean. The capital, Roseau, is located on the western side of the island. It is geographically situated as part of the Windward Islands chain in the Lesser Antilles archipelago in the Caribbean Sea. Dominica's closest neighbours are two constituent territories of the European Union and Eurozone, the overseas departments of the French Republic, Guadeloupe to the northwest and Martinique to the south-southeast. Dominica comprises a land area of 750 sq km (290 sq mi), and the highest point is Morne Diablotins, at 1,447 m (4,747 ft) in elevation. The population was 71,293 at the 2011 census.",inline=False)
  embed.add_field(name="Capital",value="Roseau",inline=False)
  embed.add_field(name="Flag",value="<:flag_dm:968444587117002763>",inline=False)
  embed.add_field(name="Population",value="71,625",inline=False)
  embed.add_field(name="GDP (PPP)",value="$688 billion",inline=False)
  embed.add_field(name="Currency",value="East Carribean dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -4",inline=False)
  embed.add_field(name="Dialing Code",value="+1-767",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def DominicanRepublic(ctx):
  embed=discord.Embed(title="Dominican Republic",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="The Dominican Republic, is a country located on the island of Hispaniola in the Greater Antilles archipelago of the Caribbean region. It occupies the eastern five-eighths of the island, which it shares with Haiti, making Hispaniola one of only two Caribbean islands, along with Saint Martin, that is shared by two sovereign states. The Dominican Republic is the second-largest nation in the Antilles by area (after Cuba) at 48,671 square kilometers (18,792 sq mi), and third-largest by population, with approximately 10.8 million people (2020 est.), of whom approximately 3.3 million live in the metropolitan area of Santo Domingo, the capital city. The official language of the country is Spanish.",inline=False)
  embed.add_field(name="Capital",value="Santo Domingo",inline=False)
  embed.add_field(name="Flag",value="<:flag_do:968446044964814858>",inline=False)
  embed.add_field(name="Population",value="10.87 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$215.99 billion",inline=False)
  embed.add_field(name="Currency",value="Dominican peso",inline=False)
  embed.add_field(name="Time Zone",value="UTC -4",inline=False)
  embed.add_field(name="Dialing Code",value="+1-809",inline=False)
  await ctx.send(embed=embed)



#Countries Staring with E
@client.command()
async def Ecuador(ctx):
  embed=discord.Embed(title="Ecuador",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Ecuador, officially the Republic of Ecuador (Spanish: República del Ecuador, which literally translates as Republic of the Equator; Quechua: Ikwadur Ripuwlika; Shuar: Ekuatur Nunka), is a country in northwestern South America, bordered by Colombia on the north, Peru on the east and south, and the Pacific Ocean on the west. Ecuador also includes the Galápagos Islands in the Pacific, about 1,000 kilometers (621 mi) west of the mainland. The capital is Quito.",inline=False)
  embed.add_field(name="Capital",value="Quito",inline=False)
  embed.add_field(name="Flag",value="<:flag_ec:968450009039253574>",inline=False)
  embed.add_field(name="Population",value="17.71 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$202.04 billion",inline=False)
  embed.add_field(name="Currency",value="United States dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -5 or UTC -6",inline=False)
  embed.add_field(name="Dialing Code",value="+593",inline=False)
  await ctx.send(embed=embed)

  

@client.command()
async def Egypt(ctx):
  embed=discord.Embed(title="Egypt",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Egypt, officially the Arab Republic of Egypt, is a transcontinental country spanning the northeast corner of Africa and southwest corner of Asia via a land bridge formed by the Sinai Peninsula. It is bordered by the Mediterranean Sea to the north, the Gaza Strip (Palestine) and Israel to the northeast, the Red Sea to the east, Sudan to the south, and Libya to the west. The Gulf of Aqaba in the northeast separates Egypt from Jordan and Saudi Arabia. Cairo is the capital and largest city of Egypt, while Alexandria, the second-largest city, is an important industrial and tourist hub at the Mediterranean coast. At approximately 100 million inhabitants, Egypt is the 14th-most populated country in the world.",inline=False)
  embed.add_field(name="Capital",value="Cairo",inline=False)
  embed.add_field(name="Flag",value="<:flag_eg:968450816568594483>",inline=False)
  embed.add_field(name="Population",value="102.67 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.49 trillion",inline=False)
  embed.add_field(name="Currency",value="Egyptian pound",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+20",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def ElSalvador(ctx):
  embed=discord.Embed(title="El Salvador",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="El Salvador, officially the Republic of El Salvador (Spanish: República de El Salvador), is a country in Central America. It is bordered on the northeast by Honduras, on the northwest by Guatemala, and on the south by the Pacific Ocean. El Salvador's capital and largest city is San Salvador. The country's population in 2021 is estimated to be 6.8 million.",inline=False)
  embed.add_field(name="Capital",value="San Salvador",inline=False)
  embed.add_field(name="Flag",value="<:flag_sv:968451367733702706>",inline=False)
  embed.add_field(name="Population",value="6.83 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$57.95 billion",inline=False)
  embed.add_field(name="Currency",value="United States dollar and Bitcoin",inline=False)
  embed.add_field(name="Time Zone",value="UTC -6",inline=False)
  embed.add_field(name="Dialing Code",value="+503",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def EquatorialGuinea(ctx):
  embed=discord.Embed(title="Equatorial Guinea",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Equatorial Guinea, officially the Republic of Equatorial Guinea (Spanish: República de Guinea Ecuatorial, French: République de Guinée équatoriale, Portuguese: República da Guiné Equatorial), is a country on the west coast of Central Africa, with an area of 28,000 square kilometres (11,000 sq mi). Formerly the colony of Spanish Guinea, its post-independence name evokes its location near both the Equator and the Gulf of Guinea. As of 2021, the country had a population of 1,468,777.",inline=False)
  embed.add_field(name="Capital",value="Malabo",inline=False)
  embed.add_field(name="Flag",value="<:flag_gp:968453434409885706>",inline=False)
  embed.add_field(name="Population",value="1.46 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$27.95 billion",inline=False)
  embed.add_field(name="Currency",value="Central African CFA franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1",inline=False)
  embed.add_field(name="Dialing Code",value="+240",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Eritrea(ctx):
  embed=discord.Embed(title="Eritrea",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Eritrea, officially the State of Eritrea, is a country in the Horn of Africa region of Eastern Africa, with its capital (and largest city) at Asmara. It is bordered by Ethiopia in the south, Sudan in the west, and Djibouti in the southeast. The northeastern and eastern parts of Eritrea have an extensive coastline along the Red Sea. The nation has a total area of approximately 117,600 sq km (45,406 sq mi), and includes the Dahlak Archipelago and several of the Hanish Islands.",inline=False)
  embed.add_field(name="Flag",value="<:flag_er:968454331126939648>",inline=False)
  embed.add_field(name="Population",value="3.6 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$6.88 billion",inline=False)
  embed.add_field(name="Currency",value="Nakfa",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+291",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Estonia(ctx):
  embed=discord.Embed(title="Estonia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Estonia, officially the Republic of Estonia (Estonian: Eesti Vabariik), is a country in Northern Europe. It is bordered to the north by the Gulf of Finland across from Finland, to the west by the Baltic Sea across from Sweden, to the south by Latvia, and to the east by Lake Peipus and Russia. The territory of Estonia consists of the mainland, the larger islands of Saaremaa and Hiiumaa, and over 2,200 other islands and islets on the eastern coast of the Baltic Sea, covering a total area of 45,339 square kilometres (17,505 sq mi). The capital city Tallinn and Tartu are the two largest urban areas of the country. The Estonian language is the autochthonous and the official language of Estonia; it is the first language of the majority of its people, as well as the world's second most spoken Finnic language.",inline=False)
  embed.add_field(name="Capital",value="Tallinn",inline=False)
  embed.add_field(name="Flag",value="<:flag_ee:968455283212967986>",inline=False)
  embed.add_field(name="Population",value="1.32 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$59.55 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2 to UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+372",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Estiwani(ctx):
  embed=discord.Embed(title="Estiwani",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Estiwani, officially the Kingdom of Eswatini and formerly named in English as Swaziland (/ˈswɑːzilænd/ SWAH-zee-land; officially renamed in 2018), is a landlocked country in Southern Africa. It is bordered by Mozambique to its northeast and South Africa to its north, west, south, and southeast. At no more than 200 kilometres (120 mi) north to south and 130 kilometres (81 mi) east to west, Eswatini is one of the smallest countries in Africa; despite this, its climate and topography are diverse, ranging from a cool and mountainous highveld to a hot and dry lowveld",inline=False)
  embed.add_field(name="Capital",value="Mbabane",inline=False)
  embed.add_field(name="Flag",value="<:flag_sz:968456102301814834>",inline=False)
  embed.add_field(name="Population",value="1.16 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$10.71 billion",inline=False)
  embed.add_field(name="Currency",value="Lilangeni",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+268",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Ethiopia(ctx):
  embed=discord.Embed(title="Ethiopia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Ethiopia, officially the Federal Democratic Republic of Ethiopia, is a landlocked country in the Horn of Africa. It shares borders with Eritrea and Djibouti to the north, Somalia to the east and northeast, Kenya to the south, South Sudan to the west, and Sudan to the northwest. Ethiopia has a total area of 1,100,000 square kilometres (420,000 sq mi). It is home to 117 million inhabitants and is the 12th-most populous country in the world and the 2nd-most populous in Africa after Nigeria. The national capital and largest city, Addis Ababa, lies several kilometres west of the East African Rift that splits the country into the African and Somali tectonic plates.",inline=False)
  embed.add_field(name="Capital",value="Addis Ababa",inline=False)
  embed.add_field(name="Flag",value="<:flag_et:968456970971512903>",inline=False)
  embed.add_field(name="Population",value="117.87 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$401 billion",inline=False)
  embed.add_field(name="Currency",value="Birr",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+251",inline=False)
  await ctx.send(embed=embed)



#Countries starting with F
@client.command()
async def Fiji(ctx):
  embed=discord.Embed(title="Fiji",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Fiji is an island country in Melanesia, part of Oceania in the South Pacific Ocean. It lies about 1,100 nautical miles (2,000 km; 1,300 mi) northeast of New Zealand. Fiji consists of an archipelago of more than 330 islands—of which about 110 are permanently inhabited—and more than 500 islets, amounting to a total land area of about 18,300 square kilometres (7,100 sq mi). The most outlying island group is Ono-i-Lau. About 87% of the total population of 883,483 live on the two major islands, Viti Levu and Vanua Levu. About three-quarters of Fijians live on Viti Levu's coasts: either in the capital city of Suva; or in smaller urban centres such as Nadi—where tourism is the major local industry; or in Lautoka, where the sugar-cane industry is dominant. The interior of Viti Levu is sparsely inhabited because of its terrain.",inline=False)
  embed.add_field(name="Capital",value="Suva",inline=False)
  embed.add_field(name="Flag",value="<:flag_fj:968457857953562685>",inline=False)
  embed.add_field(name="Population",value="926,627",inline=False)
  embed.add_field(name="GDP (PPP)",value="$9.11 billion",inline=False)
  embed.add_field(name="Currency",value="Fijian dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +12 or UTC +13",inline=False)
  embed.add_field(name="Dialing Code",value="+679",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Finland(ctx):
  embed=discord.Embed(title="Finland",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Finland, officially the Republic of Finland (Finnish: Suomen tasavalta; Swedish: Republiken Finland (listen to all)),[note 1] is a Nordic country in Northern Europe. It shares land borders with Sweden to the northwest, Norway to the north, and Russia to the east, with the Gulf of Bothnia to the west and the Gulf of Finland across Estonia to the south. Finland covers an area of 338,455 square kilometres (130,678 sq mi) with a population of 5.5 million. Helsinki is the capital and largest city, forming a larger metropolitan area with the neighbouring cities of Espoo, Kauniainen, and Vantaa. The vast majority of the population are ethnic Finns; Finnish is an official language alongside Swedish are official languages. Finland's climate varies from humid continental in the south to the boreal in the north. The land cover is primarily a boreal forest biome, with more than 180,000 recorded lakes.",inline=False)
  embed.add_field(name="Capital",value="Helsinki",inline=False)
  embed.add_field(name="Flag",value="<:flag_fi:968458441532256277>",inline=False)
  embed.add_field(name="Population",value="5.53 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$257 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2 or UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+358",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def France(ctx):
  embed=discord.Embed(title="France",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="France, officially the French Republic is a transcontinental country spanning Western Europe and the overseas regions and territories in the Americas and the Atlantic, Pacific and Indian Oceans. Its metropolitan area extends from the Rhine to the Atlantic Ocean and from the Mediterranean Sea to the English Channel and the North Sea; overseas territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many islands in Oceania and the Indian Ocean. Due to its several coastal territories, France has the largest exclusive economic zone in the world. France borders Belgium, Luxembourg, Germany, Switzerland, Monaco, Italy, Andorra, and Spain in Europe, as well as the Netherlands, Suriname, and Brazil in the Americas via its overseas territory in French Guiana. Its eighteen integral regions (five of which are overseas) span a combined area of 643,801 sq km (248,573 sq mi) and over 67 million people (as of May 2021). France is a unitary semi-presidential republic with its capital in Paris, the country's largest city and main cultural and commercial centre; other major urban areas include Marseille, Lyon, Toulouse, Lille, Bordeaux, and Nice. ",inline=False)
  embed.add_field(name="Capital",value="Paris",inline=False)
  embed.add_field(name="Flag",value="<:flag_fr:968459174793076776>",inline=False)
  embed.add_field(name="Population",value="67.41 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$3.32 trillion and CFP franc",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+33",inline=False)
  await ctx.send(embed=embed)  
  

  
 #Countries Starting with G
@client.command()
async def Gabon(ctx):
  embed=discord.Embed(title="Gabon",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Gabon, officially the Gabonese Republic (French: République gabonaise), is a country on the west coast of Central Africa. Located on the equator, Gabon is bordered by Equatorial Guinea to the northwest, Cameroon to the north, the Republic of the Congo on the east and south, and the Gulf of Guinea to the west. It has an area of nearly 270,000 square kilometres (100,000 sq mi) and its population is estimated at 2.1 million people. There are three distinct regions: the coastal plains, the mountains (the Cristal Mountains and the Chaillu Massif in the centre), and the savanna in the east. Gabon's capital and largest city is Libreville. The official language is French.",inline=False)
  embed.add_field(name="Capital",value="Libreville",inline=False)
  embed.add_field(name="Flag",value="<:flag_ga:968471203213901864>",inline=False)
  embed.add_field(name="Population",value="2.11 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$37.82 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1",inline=False)
  embed.add_field(name="Dialing Code",value="+241",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def TheGambia(ctx):
  embed=discord.Embed(title="The Gambia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="The Gambia, officially the Republic of The Gambia, is a country in West Africa. It is the smallest country within mainland Africa and is surrounded by Senegal, except for its western coast on the Atlantic Ocean. The Gambia is situated on both sides of the lower reaches of the Gambia River, the nation's namesake, which flows through the centre of the Gambia and empties into the Atlantic Ocean. It has an area of 10,689 square kilometres (4,127 sq mi) with a population of 1,857,181 as of the April 2013 census. Banjul is the Gambian capital and the country's largest metropolitan area. The largest cities are Serekunda and Brikama.",inline=False)
  embed.add_field(name="Capital",value="Banjul",inline=False)
  embed.add_field(name="Flag",value="<:flag_gm:968473190592553041>",inline=False)
  embed.add_field(name="Population",value="2.17 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$5.42 billion",inline=False)
  embed.add_field(name="Currency",value="Dalasi",inline=False)
  embed.add_field(name="Time Zone",value="UTC",inline=False)
  embed.add_field(name="Dialing Code",value="+220",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Georgia(ctx):
  embed=discord.Embed(title="Georgia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Georgia, is a country located in the Caucasus, at the intersection of Eastern Europe and Western Asia. It is bounded by the Black Sea to the west, by Russia to the north and east, by Turkey to the southwest, by Armenia to the south, and by Azerbaijan to the southeast. The country covers an area of 69,700 square kilometres (26,900 sq mi), and has a population of 3.7 million people (excluding the Russian-occupied Georgian territories). Georgia is a representative democracy governed as a unitary parliamentary republic. Tbilisi is its capital as well as its largest city, and is home to roughly a third of the Georgian population.",inline=False)
  embed.add_field(name="Capital",value="Tbilisi",inline=False)
  embed.add_field(name="Flag",value="<:flag_ge:968473634278621184>",inline=False)
  embed.add_field(name="Population",value="3.72 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$61.58 million",inline=False)
  embed.add_field(name="Currency",value="Georgian lari",inline=False)
  embed.add_field(name="Time Zone",value="UTC +4",inline=False)
  embed.add_field(name="Dialing Code",value="+995",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Germany(ctx):
  embed=discord.Embed(title="Germany",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Germany, officially the Federal Republic of Germany, is a country in Central Europe. It is the second most populous country in Europe after Russia, and the most populous member state of the European Union. Germany is situated between the Baltic and North seas to the north, and the Alps to the south; it covers an area of 357,022 square kilometres (137,847 sq mi), with a population of over 83 million within its 16 constituent states. Germany borders Denmark to the north, Poland and the Czech Republic to the east, Austria and Switzerland to the south, and France, Luxembourg, Belgium, and the Netherlands to the west. The nation's capital and largest city is Berlin, and its financial centre is Frankfurt; the largest urban area is the Ruhr.",inline=False)
  embed.add_field(name="Capital",value="Berlin",inline=False)
  embed.add_field(name="Flag",value="<:flag_de:968474812718665738>",inline=False)
  embed.add_field(name="Population",value="83.19 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$4.31 trillion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+49",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Ghana(ctx):
  embed=discord.Embed(title="Ghana",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Ghana, officially the Republic of Ghana, is a country in West Africa. It spans the Gulf of Guinea and the Atlantic Ocean to the south, sharing borders with the Ivory Coast in the west, Burkina Faso in the north, and Togo in the east. Ghana covers an area of 238,535 sq km (92,099 sq mi), spanning diverse biomes that range from coastal savannas to tropical rain forests. With over 31 million people, Ghana is the second-most populous country in West Africa, after Nigeria. The capital and largest city is Accra; other major cities are Kumasi, Tamale, and Sekondi-Takoradi.",inline=False)
  embed.add_field(name="Capital",value="Accra",inline=False)
  embed.add_field(name="Flag",value="<:flag_gh:968475477473910785>",inline=False)
  embed.add_field(name="Population",value="32.10 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$226 billion",inline=False)
  embed.add_field(name="Currency",value="Cedi",inline=False)
  embed.add_field(name="Time Zone",value="UTC",inline=False)
  embed.add_field(name="Dialing Code",value="+233",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Greece(ctx):
  embed=discord.Embed(title="Greece",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Greece, officially the Hellenic Republic, is a country in Southeast Europe. It is situated on the southern tip of the Balkans, and is located at the crossroads of Europe, Asia, and Africa. Greece shares land borders with Albania to the northwest, North Macedonia and Bulgaria to the north, and Turkey to the northeast. The Aegean Sea lies to the east of the mainland, the Ionian Sea to the west, and the Sea of Crete and the Mediterranean Sea to the south. Greece has the longest coastline on the Mediterranean Basin, featuring thousands of islands. The country consists of nine traditional geographic regions, and has a population of approximately 10.7 million. Athens is the nation's capital and largest city, followed by Thessaloniki. ",inline=False)
  embed.add_field(name="Capital",value="Athens",inline=False)
  embed.add_field(name="Flag",value="<:flag_gr:968476274072911903>",inline=False)
  embed.add_field(name="Population",value="10.67 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$378.69 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2 or UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+30",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Grenada(ctx):
  embed=discord.Embed(title="Grenada",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Grenada, is an island country in the West Indies in the Caribbean Sea at the southern end of the Grenadines island chain. Grenada consists of the island of Grenada itself, two smaller islands, Carriacou and Petite Martinique, and several small islands which lie to the north of the main island and are a part of the Grenadines. It is located northwest of Trinidad and Tobago, northeast of Venezuela and southwest of Saint Vincent and the Grenadines. Its size is 348.5 square kilometres (134.6 sq mi), and it had an estimated population of 112,523 in July 2020. Its capital is St. George's. Grenada is also known as the Island of Spice due to its production of nutmeg and mace crops.",inline=False)
  embed.add_field(name="Capital",value="St. George's",inline=False)
  embed.add_field(name="Flag",value="<:flag_gd:968477117568385024>",inline=False)
  embed.add_field(name="Population",value="111,454",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.8 billion",inline=False)
  embed.add_field(name="Currency",value="East Carribean dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -4",inline=False)
  embed.add_field(name="Dialing Code",value="+1-473",inline=False)
  await ctx.send(embed=embed)




@client.command()
async def Guatemala(ctx):
  embed=discord.Embed(title="Guatemala",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Guatemala, officially the Republic of Guatemala (Spanish: República de Guatemala), is a country in Central America, bordered by Mexico to the north and west, Belize and the Caribbean to the northeast, Honduras to the east, El Salvador to the southeast and the Pacific Ocean to the south. With an estimated population of around 17.2 million, it is the most populous country in Central America and is the 11th most populous country in the Americas. Guatemala is a representative democracy; its capital and largest city is Nueva Guatemala de la Asunción, also known as Guatemala City, the largest city in Central America. ",inline=False)
  embed.add_field(name="Capital",value="Guatemala City",inline=False)
  embed.add_field(name="Flag",value="<:flag_gt:968477683119951922>",inline=False)
  embed.add_field(name="Population",value="17.26 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$145.24 billion",inline=False)
  embed.add_field(name="Currency",value="Quetzal",inline=False)
  embed.add_field(name="Time Zone",value="UTC -6",inline=False)
  embed.add_field(name="Dialing Code",value="+502",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Guinea(ctx):
  embed=discord.Embed(title="Guinea",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Guinea, officially the Republic of Guinea (French: République de Guinée; Pular: 𞤈𞤫𞤲𞤣𞤢𞥄𞤲𞤣𞤭 𞤘𞤭𞤲𞤫; N'Ko: ߖߌ߬ߣߍ߫), is a coastal country in West Africa. Guinea borders the Atlantic Ocean to the west, Guinea-Bissau to the northwest, Senegal to the north, Mali to the northeast, Cote d'Ivoire to the southeast, and Sierra Leone and Liberia to the south. Formerly known as French Guinea (French: Guinée française), the modern country is sometimes referred to as Guinea-Conakry after its capital Conakry, to distinguish it from other territories in the eponymous region such as Guinea-Bissau and Equatorial Guinea. Guinea has a population of 12.4 million and an area of 245,857 square kilometres (94,926 sq mi).",inline=False)
  embed.add_field(name="Capital",value="Conakry",inline=False)
  embed.add_field(name="Flag",value="<:flag_gn:968478912063623228>",inline=False)
  embed.add_field(name="Population",value="12.41 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$26.45 billion",inline=False)
  embed.add_field(name="Currency",value="Guinean franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC",inline=False)
  embed.add_field(name="Dialing Code",value="+224",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def GuineaBissau(ctx):
  embed=discord.Embed(title="Guinea Bissau",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Guinea Bissau, officially the Republic of Guinea-Bissau (Portuguese: República da Guiné-Bissau [ʁɛˈpuβlikɐ ðɐ ɣiˈnɛ βiˈsaw]), is a country in West Africa that covers 36,125 square kilometres (13,948 sq mi) with an estimated population of 1,726,000. It borders Senegal to the north and Guinea to the south-east.",inline=False)
  embed.add_field(name="Capital",value="Bissau",inline=False)
  embed.add_field(name="Flag",value="<:flag_gw:968479395125821440>",inline=False)
  embed.add_field(name="Population",value="1.72 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$3.8 billion",inline=False)
  embed.add_field(name="Currency",value="West African CFA franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC",inline=False)
  embed.add_field(name="Dialing Code",value="+245",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Guyana(ctx):
  embed=discord.Embed(title="Guyana",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Guyana, officially the Co‑operative Republic of Guyana, is a country on the northern mainland of South America. The capital city is Georgetown. Guyana is bordered by the Atlantic Ocean to the north, Brazil to the south and southwest, Venezuela to the west, and Suriname to the east. With 215,000 square kilometres (83,000 sq mi), Guyana is the third-smallest sovereign state by area in mainland South America after Uruguay and Suriname, and is the second-least populous sovereign state in South America after Suriname; it is also one of the least densely populated countries on Earth. It has a wide variety of natural habitats and very high biodiversity.",inline=False)
  embed.add_field(name="Capital",value="Georgetown",inline=False)
  embed.add_field(name="Flag",value="<:flag_gy:968480194467864606>",inline=False)
  embed.add_field(name="Population",value="743,700",inline=False)
  embed.add_field(name="GDP (PPP)",value="$18.35 billion",inline=False)
  embed.add_field(name="Currency",value="Guyanese dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -4",inline=False)
  embed.add_field(name="Dialing Code",value="+592",inline=False)
  await ctx.send(embed=embed) 
  
 

#Countries starting with H
@client.command()
async def Haiti(ctx):
  embed=discord.Embed(title="Haiti",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Haiti, officially the Republic of Haiti (French: République d'Haïti; Haitian Creole: Repiblik d Ayiti),[11] and formerly known as Hayti,[note 1] is a country located on the island of Hispaniola in the Greater Antilles archipelago of the Caribbean Sea, to the east of Cuba and Jamaica and south of The Bahamas and the Turks and Caicos Islands. It occupies the western three-eighths of the island which it shares with the Dominican Republic. To its south-west lies the small Navassa Island, which is claimed by Haiti but is disputed as a United States territory under federal administration.[19][20] Haiti is 27,750 sq km (10,714 sq mi) in size, the third largest country in the Caribbean by area, and has an estimated population of 11.4 million, making it the most populous country in the Caribbean. The capital is Port-au-Prince",inline=False)
  embed.add_field(name="Capital",value="Port-au-Prince",inline=False)
  embed.add_field(name="Flag",value="<:flag_ht:968486556711157810>",inline=False)
  embed.add_field(name="Population",value="11.43 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$34.18 billion",inline=False)
  embed.add_field(name="Currency",value="Gourde",inline=False)
  embed.add_field(name="Time Zone",value="UTC -5 to UTC -4",inline=False)
  embed.add_field(name="Dialing Code",value="+509",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Honduras(ctx):
  embed=discord.Embed(title="Honduras",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Honduras, officially the Republic of Honduras, is a country in Central America. The republic of Honduras is bordered to the west by Guatemala, to the southwest by El Salvador, to the southeast by Nicaragua, to the south by the Pacific Ocean at the Gulf of Fonseca, and to the north by the Gulf of Honduras, a large inlet of the Caribbean Sea. Its capital and largest city is Tegucigalpa.",inline=False)
  embed.add_field(name="Capital",value="Tegucigalpa",inline=False)
  embed.add_field(name="Flag",value="<:flag_hn:968487993008599120>",inline=False)
  embed.add_field(name="Population",value="9.58 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$49.01 billion",inline=False)
  embed.add_field(name="Currency",value="Lempira",inline=False)
  embed.add_field(name="Time Zone",value="UTC -6",inline=False)
  embed.add_field(name="Dialing Code",value="+504",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Hungary(ctx):
  embed=discord.Embed(title="Hungary",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Hungary, Hungary (Hungarian: Magyarország [ˈmɒɟɒrorsaːɡ]) is a landlocked country in Central Europe. Spanning 93,030 square kilometres (35,920 sq mi) of the Carpathian Basin, it is bordered by Slovakia to the north, Ukraine to the northeast, Romania to the east and southeast, Serbia to the south, Croatia and Slovenia to the southwest and Austria to the west. Hungary has a population of nearly 10 million, mostly ethnic Hungarians and a significant Romani minority. Hungarian, the official language, is the world's most widely spoken Uralic language and among the few non-Indo-European languages widely spoken in Europe. Budapest is the country's capital and largest city; other major urban areas include Debrecen, Szeged, Miskolc, Pécs and Győr.",inline=False)
  embed.add_field(name="Capital",value="Budapest",inline=False)
  embed.add_field(name="Flag",value="<:flag_hu:968489326172315749>",inline=False)
  embed.add_field(name="Population",value="9.73 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$359.90 billion",inline=False)
  embed.add_field(name="Currency",value="Forint",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+36",inline=False)
  await ctx.send(embed=embed)



  
 #Countries starting with I
@client.command()
async def Iceland(ctx):
  embed=discord.Embed(title="Iceland",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Iceland is a Nordic island country in the North Atlantic Ocean and the most sparsely populated country in Europe. Iceland's capital and largest city is Reykjavík, which (along with its surrounding areas) is home to over 65% of the population. Iceland is the only part of the Mid-Atlantic Ridge that rises above sea level, and its central volcanic plateau is erupting almost constantly. The interior consists of a plateau characterised by sand and lava fields, mountains, and glaciers, and many glacial rivers flow to the sea through the lowlands. Iceland is warmed by the Gulf Stream and has a temperate climate, despite a high latitude just outside the Arctic Circle. Its high latitude and marine influence keep summers chilly, and most of its islands have a polar climate.",inline=False)
  embed.add_field(name="Capital",value="Reykjavik",inline=False)
  embed.add_field(name="Flag",value="<:flag_is:968536646209380432>",inline=False)
  embed.add_field(name="Population",value="371,580",inline=False)
  embed.add_field(name="GDP (PPP)",value="$19.8 billion",inline=False)
  embed.add_field(name="Currency",value="Icelandic krona",inline=False)
  embed.add_field(name="Time Zone",value="UTC",inline=False)
  embed.add_field(name="Dialing Code",value="+354",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def India(ctx):
  embed=discord.Embed(title="India",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="India, officially the Republic of India (Hindi: Bhārat Gaṇarājya), is a country in South Asia. It is the seventh-largest country by area, the second-most populous country, and the most populous democracy in the world. Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[f] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar and Indonesia. ",inline=False)
  embed.add_field(name="Capital",value="New Delhi",inline=False)
  embed.add_field(name="Flag",value="<:flag_in:968537125421215804>",inline=False)
  embed.add_field(name="Population",value="1.35 billion",inline=False)
  embed.add_field(name="GDP (PPP)",value="$11.74 trillion",inline=False)
  embed.add_field(name="Currency",value="Indian rupee",inline=False)
  embed.add_field(name="Time Zone",value="UTC +5:30",inline=False)
  embed.add_field(name="Dialing Code",value="+91",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Indonesia(ctx):
  embed=discord.Embed(title="Indonesia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Indonesia, officially the Republic of Indonesia, is a country in Southeast Asia and Oceania between the Indian and Pacific oceans. It consists of over 17,000 islands, including Sumatra, Java, Sulawesi, and parts of Borneo and New Guinea. Indonesia is the world's largest island country and the 14th-largest country by area, at 1,904,569 square kilometres (735,358 square miles). With about 270 million people, Indonesia is the world's fourth-most populous country and the most populous Muslim-majority country. Java, the world's most populous island, is home to more than half of the country's population.",inline=False)
  embed.add_field(name="Capital",value="Jakarta",inline=False)
  embed.add_field(name="Flag",value="<:flag_id:968545135581356134>",inline=False)
  embed.add_field(name="Population",value="273.87 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$3.99 trillion",inline=False)
  embed.add_field(name="Currency",value="Indonesian rupiah",inline=False)
  embed.add_field(name="Time Zone",value="UTC +7 to UTC +9",inline=False)
  embed.add_field(name="Dialing Code",value="+62",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Iran(ctx):
  embed=discord.Embed(title="Iran",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Iran, also called Persia, and officially the Islamic Republic of Iran, is a country in Western Asia. It is bordered to the west by Iraq and Turkey, to the northwest by Azerbaijan and Armenia, to the north by the Caspian Sea and Turkmenistan, to the east by Afghanistan and Pakistan, and to the south by the Gulf of Oman and the Persian Gulf. Iran covers an area of 1,648,195 sq km (636,372 sq mi), making it the fourth-largest country entirely in Asia and the second-largest in Western Asia. It has a population of 85 million, making it the 17th-most populous country in the world. Its capital and largest city is Tehran.",inline=False)
  embed.add_field(name="Capital",value="Tehran",inline=False)
  embed.add_field(name="Flag",value="<:flag_ir:968545969648058448>",inline=False)
  embed.add_field(name="Population",value="83.18 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.57 trillion",inline=False)
  embed.add_field(name="Currency",value="Iranian rial",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3:30 or UTC +4:30",inline=False)
  embed.add_field(name="Dialing Code",value="+98",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Iraq(ctx):
  embed=discord.Embed(title="Iraq",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Iraq, officially the Republic of Iraq (Arabic: جُمْهُورِيَّة ٱلْعِرَاق Jumhūriīyet al-ʿIrāq; Kurdish: کۆماری عێراق, romanized: Komarî Êraq), is a country in Western Asia. It is bordered by Turkey to the north, Iran to the east, the Persian Gulf and Kuwait to the southeast, Saudi Arabia to the south, Jordan to the southwest and Syria to the west. The capital and largest city is Baghdad. Iraq is home to diverse ethnic groups including Mesopotamian Arabs, Kurds, Turkmens, Assyrians, Armenians, Yazidis, Sabian-Mandaeans, Persians and Shabakis with similarly diverse geography and wildlife. The majority of the country's 40 million citizens are Muslims, and other recognized religions include Christianity, Yazidism, Mandaeism, Yarsanism and Zoroastrianism The official languages of Iraq are Arabic and Kurdish, with other recognized regional languages being English, Neo-Aramaic, Turkish and Armenian.",inline=False)
  embed.add_field(name="Capital",value="Baghdad",inline=False)
  embed.add_field(name="Flag",value="<:flag_iq:968551427104444466>",inline=False)
  embed.add_field(name="Population",value="40.22 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$413.31 billion",inline=False)
  embed.add_field(name="Currency",value="Iraqi dinar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+964",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Ireland(ctx):
  embed=discord.Embed(title="Ireland",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Ireland, also known as the Republic of Ireland (Poblacht na hÉireann), is a country in north-western Europe consisting of 26 of the 32 counties of the island of Ireland. The capital and largest city is Dublin, on the eastern side of the island. Around 40% of the country's population of 5 million people resides in the Greater Dublin Area. The sovereign state shares its only land border with Northern Ireland, which is part of the United Kingdom. It is otherwise surrounded by the Atlantic Ocean, with the Celtic Sea to the south, St George's Channel to the south-east, and the Irish Sea to the east. It is a unitary, parliamentary republic.",inline=False)
  embed.add_field(name="Capital",value="Dublin",inline=False)
  embed.add_field(name="Flag",value="<:flag_ie:968553309738786846>",inline=False)
  embed.add_field(name="Population",value="5.01 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$561 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC or UTC +1",inline=False)
  embed.add_field(name="Dialing Code",value="+353",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Israel(ctx):
  embed=discord.Embed(title="Israel",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Israel, officially the State of Israel (מְדִינַת יִשְׂרָאֵל, Medīnat Yīsrāʾēl; دَوْلَة إِسْرَائِيل, Dawlat ʾIsrāʾīl), is a country in Western Asia. It is situated on the southeastern shore of the Mediterranean Sea and the northern shore of the Red Sea, and shares borders with Lebanon to the north, Syria to the northeast, Jordan to the east, and Egypt to the southwest; it is also bordered by the Palestinian territories of the West Bank and the Gaza Strip to the east and west, respectively. Tel Aviv is the economic and technological center of the country, while its seat of government is in its proclaimed capital of Jerusalem, although Israeli sovereignty over East Jerusalem is unrecognized internationally.",inline=False)
  embed.add_field(name="Capital",value="Tel Aviv (Jerusalem is not completely recognized as the capital)",inline=False)
  embed.add_field(name="Flag",value="<:flag_il:968554260633636884>",inline=False)
  embed.add_field(name="Population",value="9.5 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$478.01 billion",inline=False)
  embed.add_field(name="Currency",value="New shekel",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2 or UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+972",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Italy(ctx):
  embed=discord.Embed(title="Italy",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Italy, officially the Italian Republic or Republic of Italy (Italian: Repubblica Italiana [reˈpubblika itaˈljaːna]), is a country consisting of a peninsula delimited by the Alps and several islands surrounding it, whose territory largely coincides with the homonymous geographical region. Italy is located in the middle of the Mediterranean Sea, in Southern Europe; it is also considered part of Western Europe. A unitary parliamentary republic with Rome as its capital and largest city, the country covers a total area of 301,230 sq km (116,310 sq mi) and shares land borders with France, Switzerland, Austria, Slovenia, as well as the enclaved microstates of Vatican City and San Marino. Italy has a territorial exclave in Switzerland, Campione. With over 60 million inhabitants, Italy is the third-most populous member state of the European Union.",inline=False)
  embed.add_field(name="Capital",value="Rome",inline=False)
  embed.add_field(name="Flag",value="<:flag_it:968555011548250223>",inline=False)
  embed.add_field(name="Population",value="60.31 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$2.61 trillion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+39",inline=False)
  await ctx.send(embed=embed)



#Countries starting with J
@client.command()
async def Jamaica(ctx):
  embed=discord.Embed(title="Jamaica",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Jamaica, is an island country situated in the Caribbean Sea. Spanning 10,990 square kilometres (4,240 sq mi) in area, it is the third-largest island of the Greater Antilles and the Caribbean (after Cuba and Hispaniola). Jamaica lies about 145 kilometres (90 mi) south of Cuba, and 191 kilometres (119 mi) west of Hispaniola (the island containing the countries of Haiti and the Dominican Republic); the British Overseas Territory of the Cayman Islands lies some 215 kilometres (134 mi) to the north-west.",inline=False)
  embed.add_field(name="Capital",value="Kingston",inline=False)
  embed.add_field(name="Flag",value="<:flag_jm:968555950829076501>",inline=False)
  embed.add_field(name="Population",value="2.72 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$26.98 billion",inline=False)
  embed.add_field(name="Currency",value="Jamaican dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -5",inline=False)
  embed.add_field(name="Dialing Code",value="+1-876",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Japan(ctx):
  embed=discord.Embed(title="Japan",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Japan is an island country in East Asia. It is situated in the northwest Pacific Ocean, and is bordered on the west by the Sea of Japan, while extending from the Sea of Okhotsk in the north toward the East China Sea and Taiwan in the south. Japan is a part of the Ring of Fire, and spans an archipelago of 6852 islands covering 377,975 square kilometers (145,937 sq mi); the five main islands are Hokkaido, Honshu (the mainland), Shikoku, Kyushu, and Okinawa. Tokyo is the nation's capital and largest city; other major cities include Yokohama, Osaka, Nagoya, Sapporo, Fukuoka, Kobe, and Kyoto. ",inline=False)
  embed.add_field(name="Capital",value="Tokyo",inline=False)
  embed.add_field(name="Flag",value="<:flag_jp:968556515332075570>",inline=False)
  embed.add_field(name="Population",value="125.50 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$6.11 trillion",inline=False)
  embed.add_field(name="Currency",value="Japanese yen",inline=False)
  embed.add_field(name="Time Zone",value="UTC +9",inline=False)
  embed.add_field(name="Dialing Code",value="+81",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Jordan(ctx):
  embed=discord.Embed(title="Jordan",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Jordan, officially the Hashemite Kingdom of Jordan, is a country in Western Asia. It is situated at the crossroads of Asia, Africa and Europe, within the Levant region, on the East Bank of the Jordan River. Jordan is bordered by Saudi Arabia to the south and east, Iraq to the northeast, Syria to the north, and Israel, the Palestinian West Bank, and the Dead Sea to the west. In the southwest, it has a 26 km (16 mi) coastline on the Gulf of Aqaba in the Red Sea. The Gulf of Aqaba separates Jordan from Egypt. Amman is Jordan's capital and largest city, as well as its economic, political, and cultural centre.",inline=False)
  embed.add_field(name="Capital",value="Amman",inline=False)
  embed.add_field(name="Flag",value="<:flag_jo:968557354180313118>",inline=False)
  embed.add_field(name="Population",value="11.04 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$102.15 million",inline=False)
  embed.add_field(name="Currency",value="Jordanian dinar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2 or UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+962",inline=False)
  await ctx.send(embed=embed) 
  
  
  
#Countries starting with K
@client.command()
async def Kazakhstan(ctx):
  embed=discord.Embed(title="Kazakhstan",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Kazakhstan, officially the Republic of Kazakhstan, is a transcontinental country located mainly in Central Asia and partly in Eastern Europe. It borders Russia to the north and west, China to the east, Kyrgyzstan to the southeast, Uzbekistan to the south, and Turkmenistan to the southwest. Its capital is Nur-Sultan, formerly known as Astana until 2019. Almaty, Kazakhstan's largest city, was the country's capital until 1997. Kazakhstan is the world's largest landlocked country, the world's largest Muslim-majority country by land area (and the northernmost), and the ninth-largest country in the world overall. It has a population of 19 million people, and one of the lowest population densities in the world, at fewer than 6 people per square kilometre (15 people per square mile).",inline=False)
  embed.add_field(name="Capital",value="Nur-Sultan",inline=False)
  embed.add_field(name="Flag",value="<:flag_kz:968698022336790548>",inline=False)
  embed.add_field(name="Population",value="19.08 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$569.81 billion",inline=False)
  embed.add_field(name="Currency",value="Tenge",inline=False)
  embed.add_field(name="Time Zone",value="UTC +5 or UTC +6",inline=False)
  embed.add_field(name="Dialing Code",value="+7-6 or +7-7",inline=False)
  await ctx.send(embed=embed)




@client.command()
async def Kenya(ctx):
  embed=discord.Embed(title="Kenya",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Kenya, officially the Republic of Kenya (Swahili: Jamhuri ya Kenya), is a country in Eastern Africa. At 580,367 square kilometres (224,081 sq mi), Kenya is the world's 48th largest country by area. With a population of more than 47.6 million in the 2019 census, Kenya is the 29th most populous country in the world. Kenya's capital and largest city is Nairobi, while its oldest, currently second largest city, and first capital is the coastal city of Mombasa. Kisumu City is the third-largest city and also an inland port on Lake Victoria. Other important urban centres include Nakuru and Eldoret. As of 2020, Kenya is the third-largest economy in sub-Saharan Africa after Nigeria and South Africa. Kenya is bordered by South Sudan to the northwest, Ethiopia to the north, Somalia to the east, Uganda to the west, Tanzania to the south, and the Indian Ocean to the southeast. Its geography, climate and population vary widely, ranging from cold snow-capped mountaintops (Batian, Nelion and Point Lenana on Mount Kenya) with vast surrounding forests, wildlife and fertile agricultural regions to temperate climates in western and rift valley counties and dry less fertile arid and semi-arid areas and absolute deserts (Chalbi Desert and Nyiri Desert).",inline=False)
  embed.add_field(name="Capital",value="Nairobi",inline=False)
  embed.add_field(name="Flag",value="<:flag_ke:968698916629545011>",inline=False)
  embed.add_field(name="Population",value="54.98 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$333.26 billion",inline=False)
  embed.add_field(name="Currency",value="Kenyan shilling",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+962",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Kiribati(ctx):
  embed=discord.Embed(title="Kiribati",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Kiribati, officially the Republic of Kiribati (Gilbertese: [Ribaberiki] Kiribati), is an independent island nation in the central Pacific Ocean. The permanent population is over 119,000 (2020), more than half of whom live on Tarawa atoll. The state comprises 32 atolls and one raised coral island, Banaba. There is a total land area of 811 square kilometres (313 square miles) dispersed over 3.5 million km2 (1.4 million sq mi) of ocean.",inline=False)
  embed.add_field(name="Capital",value="South Tarawa",inline=False)
  embed.add_field(name="Flag",value="<:flag_ki:968699489282039898>",inline=False)
  embed.add_field(name="Population",value="119,940",inline=False)
  embed.add_field(name="GDP (PPP)",value="$255 billion",inline=False)
  embed.add_field(name="Currency",value="Australian dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +12, UTC +13 or UTC +14",inline=False)
  embed.add_field(name="Dialing Code",value="+686",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Kuwait(ctx):
  embed=discord.Embed(title="Kuwait",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Kuwait, officially the State of Kuwait (Arabic: دولة الكويت Dawlat al-Kuwayt), is a country in Western Asia. It is situated in the northern edge of Eastern Arabia at the tip of the Persian Gulf, bordering Iraq to the north and Saudi Arabia to the south. Kuwait also shares maritime borders with Iran. Kuwait has a coastal length of approximately 500 km (311 mi). Most of the country's population reside in the urban agglomeration of the capital city Kuwait City. As of 2021, Kuwait has a population of 4.67 million people of which 1.85 million are Kuwaiti citizens while the remaining 2.8 million are foreign nationals from over 100 countries.",inline=False)
  embed.add_field(name="Capital",value="Kuwait City",inline=False)
  embed.add_field(name="Flag",value="<:flag_kw:968700251059920896>",inline=False)
  embed.add_field(name="Population",value="4.42 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$303 billion",inline=False)
  embed.add_field(name="Currency",value="Kuwaiti dinar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+965",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Kyrgyzstan(ctx):
  embed=discord.Embed(title="Kyrgyzstan",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Kyrgyzstan, officially the Kyrgyz Republic, is a mountainous landlocked country in Central Asia. Kyrgyzstan is bordered by Kazakhstan to the north, Uzbekistan to the west, Tajikistan to the south, and China to the east. Its capital and largest city is Bishkek. Ethnic Kyrgyz make up the majority of the country's six million people, followed by significant minorities of Uzbeks and Russians. The Kyrgyz language is closely related to other Turkic languages.",inline=False)
  embed.add_field(name="Capital",value="Bishkek",inline=False)
  embed.add_field(name="Flag",value="<:flag_kg:968701004319178782>",inline=False)
  embed.add_field(name="Population",value="6.58 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$37.79 billion",inline=False)
  embed.add_field(name="Currency",value="Kyrgyzstani som",inline=False)
  embed.add_field(name="Time Zone",value="UTC +6",inline=False)
  embed.add_field(name="Dialing Code",value="+996",inline=False)
  await ctx.send(embed=embed) 


  
  
  


keep_alive()
TOKEN=os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
