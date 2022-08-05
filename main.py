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
  embed.add_field(name="Capital",value="Nassau",inline=False)
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


  
#Countries Starting with L
@client.command()
async def Laos(ctx):
  embed=discord.Embed(title="Laos",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Laos, officially the Lao People's Democratic Republic, is a socialist state and the only landlocked country in Southeast Asia. At the heart of the Indochinese Peninsula, Laos is bordered by Myanmar and the People's Republic of China to the northwest, Vietnam to the east, Cambodia to the southeast, and Thailand to the west and southwest. Its capital and largest city is Vientiane.",inline=False)
  embed.add_field(name="Capital",value="Vientine",inline=False)
  embed.add_field(name="Flag",value="<:flag_la:968729298217336832>",inline=False)
  embed.add_field(name="Population",value="7.27 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$58.32 billion",inline=False)
  embed.add_field(name="Currency",value="Kip",inline=False)
  embed.add_field(name="Time Zone",value="UTC +7",inline=False)
  embed.add_field(name="Dialing Code",value="+856",inline=False)
  await ctx.send(embed=embed)




@client.command()
async def Latvia(ctx):
  embed=discord.Embed(title="Latvia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Latvia, officially the Republic of Latvia (Latvian: Latvijas Republika, Latgalian: Latvejas Republika, Livonian: Leţmō Vabāmō), is a country in the Baltic region of Northern Europe. It is one of the Baltic states; and is bordered by Estonia to the north, Lithuania to the south, Russia to the east, Belarus to the southeast, and shares a maritime border with Sweden to the west. Latvia covers an area of 64,589 sq km (24,938 sq mi), with a population of 1.9 million. The country has a temperate seasonal climate. Its capital and largest city is Riga. Latvians belong to the ethno-linguistic group of the Balts; and speak Latvian, one of the only two surviving Baltic languages. Russians are the most prominent minority in the country, at almost a quarter of the population.",inline=False)
  embed.add_field(name="Capital",value="Riga",inline=False)
  embed.add_field(name="Flag",value="<:flag_lv:968732393164918804>",inline=False)
  embed.add_field(name="Population",value="1.90 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$70.32 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2 or UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+371",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Lebanon(ctx):
  embed=discord.Embed(title="Lebanon",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Lebanon, officially the Republic of Lebanon or the Lebanese Republic, is a country in Western Asia. It is located between Syria to the north and east and Israel to the south, while Cyprus lies to its west across the Mediterranean Sea; its location at the crossroads of the Mediterranean Basin and the Arabian hinterland has contributed to its rich history and shaped a cultural identity of religious diversity. Lebanon is home to roughly six million people and covers an area of 10,452 square kilometres (4,036 sq mi), making it one of the smallest countries in the world. The official language of the state is Arabic, while French is also formally recognized; the Lebanese dialect of Arabic is used alongside Modern Standard Arabic throughout the country. ",inline=False)
  embed.add_field(name="Capital",value="Beirut",inline=False)
  embed.add_field(name="Flag",value="<:flag_lb:968733022922879016>",inline=False)
  embed.add_field(name="Population",value="6.85 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$78.91 billion",inline=False)
  embed.add_field(name="Currency",value="Lebanese pound",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2 or UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+961",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Lesotho(ctx):
  embed=discord.Embed(title="Lesotho",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Lesotho, officially the Kingdom of Lesotho (Sotho: Naha ea Lesotho), is an enclaved country surrounded by South Africa. It is a mountainous country situated in the Maloti Mountains, and contains the highest mountains in Southern Africa. Lesotho has an area of just over 30,000 sq km (11,600 sq mi) and has a population of about 2 million. Its capital and largest city is Maseru. The official languages are Sesotho and English",inline=False)
  embed.add_field(name="Capital",value="Maseru",inline=False)
  embed.add_field(name="Flag",value="<:flag_ls:968733562075480074>",inline=False)
  embed.add_field(name="Population",value="2.10 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$5.76 billion",inline=False)
  embed.add_field(name="Currency",value="Loti and South African rand",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+266",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Liberia(ctx):
  embed=discord.Embed(title="Liberia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Liberia, officially the Republic of Liberia, is a country on the West African coast. It is bordered by Sierra Leone to its northwest, Guinea to its north, Ivory Coast to its east, and the Atlantic Ocean to its south and southwest. It has a population of around 5 million and covers an area of 111,369 square kilometers (43,000 sq mi). English is the official language, but over 20 indigenous languages are spoken, reflecting the country's ethnic and cultural diversity. The country's capital and largest city is Monrovia.",inline=False)
  embed.add_field(name="Capital",value="Monrovia",inline=False)
  embed.add_field(name="Flag",value="<:flag_lr:968734196262666280>",inline=False)
  embed.add_field(name="Population",value="5.21 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$6.46 billion",inline=False)
  embed.add_field(name="Currency",value="Liberian dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC",inline=False)
  embed.add_field(name="Dialing Code",value="+231",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Libya(ctx):
  embed=discord.Embed(title="Libya",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Libya, officially the State of Libya (Arabic: دولة ليبيا, romanized: Dawlat Lībiyā), is a country in the Maghreb region in North Africa. It is bordered by the Mediterranean Sea to the north, Egypt to the east, Sudan to the southeast, Chad to the south, Niger to the southwest, Algeria to the west, and Tunisia to the northwest. Libya is made of three historical regions: Tripolitania, Fezzan, and Cyrenaica. With an area of almost 700,000 square miles (1.8 million sq km), it is the fourth-largest country in Africa and the Arab world, and the 16th-largest in the world. Libya has the 10th-largest proven oil reserves in the world. The largest city and capital, Tripoli, is located in western Libya and contains over three million of Libya's seven million people.",inline=False)
  embed.add_field(name="Capital",value="Tripoli",inline=False)
  embed.add_field(name="Flag",value="<:flag_ly:968735406126399508>",inline=False)
  embed.add_field(name="Population",value="6.99 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$90.51 billion",inline=False)
  embed.add_field(name="Currency",value="Libyan dinar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+218",inline=False)
  await ctx.send(embed=embed)

@client.command()
async def Liechtenstein(ctx):
  embed=discord.Embed(title="Liechtenstein",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Liechtenstein, officially the Principality of Liechtenstein (German: Fürstentum Liechtenstein), is a German-speaking microstate located in the Alps between Austria and Switzerland. Liechtenstein is a constitutional monarchy headed by the Prince of Liechtenstein.",inline=False)
  embed.add_field(name="Capital",value="Vaduz",inline=False)
  embed.add_field(name="Flag",value="<:flag_li:968736906705776650>",inline=False)
  embed.add_field(name="Population",value="38,896",inline=False)
  embed.add_field(name="GDP (PPP)",value="$5.3 billion",inline=False)
  embed.add_field(name="Currency",value="Swiss franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+423",inline=False)
  await ctx.send(embed=embed)

@client.command()
async def Lithuania(ctx):
  embed=discord.Embed(title="Lithuania",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Lithuania, officially the Republic of Lithuania (Lithuanian: Lietuvos Respublika), is a country in the Baltic region of Europe. It is one of three Baltic states and lies on the eastern shore of the Baltic Sea. Lithuania shares land borders with Latvia to the north, Belarus to the east and south, Poland to the south, and Kaliningrad Oblast of Russia to the southwest. It has a maritime border with Sweden to the west on the Baltic Sea. Lithuania covers an area of 65,300 sq km (25,200 sq mi), with a population of 2.8 million. Its capital and largest city is Vilnius; other major cities are Kaunas and Klaipėda. Lithuanians belong to the ethno-linguistic group of the Balts and speak Lithuanian, one of only a few living Baltic languages.",inline=False)
  embed.add_field(name="Capital",value="Vilnius",inline=False)
  embed.add_field(name="Flag",value="<:flag_lt:968737709579464734>",inline=False)
  embed.add_field(name="Population",value="2.79 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$107 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2 or UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+370",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Luxembourg(ctx):
  embed=discord.Embed(title="Luxembourg",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Luxembourg, officially the Grand Duchy of Luxembourg, is a landlocked country in Western Europe. It is bordered by Belgium to the west and north, Germany to the east, and France to the south. Its capital, Luxembourg City, is one of the four official capitals of the European Union (together with Brussels, Frankfurt, and Strasbourg) and the seat of the Court of Justice of the European Union, the highest judicial authority in the EU. Its culture, people, and languages are highly intertwined with its neighbors, making it a mixture of French and German cultures. Luxembourgish is the only national language of the Luxembourgish people, as defined by law.[11] In addition to Luxembourgish, French and German are used in administrative and judicial matters; the three languages are jointly considered administrative languages of Luxembourg.",inline=False)
  embed.add_field(name="Capital",value="Luxembourg City",inline=False)
  embed.add_field(name="Flag",value="<:flag_lu:968738330843959306>",inline=False)
  embed.add_field(name="Population",value="645,397",inline=False)
  embed.add_field(name="GDP (PPP)",value="$66.84 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+352",inline=False)
  await ctx.send(embed=embed)  
  
  
#Countries Starting with M
@client.command()
async def Madagascar(ctx):
  embed=discord.Embed(title="Madagascar",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Madagascar, officially the Republic of Madagascar (Malagasy: Repoblikan'i Madagasikara, Malagasy pronunciation: [republiˈkʲan madaɡasˈkʲarə̥]; French: République de Madagascar), and previously known as the Malagasy Republic, is an island country in the Indian Ocean, approximately 400 kilometres (250 miles) off the coast of East Africa across the Mozambique Channel. At 592,800 square kilometres (228,900 sq mi) Madagascar is the world's second-largest island country, after Indonesia. The nation consists of the island of Madagascar (the fourth-largest island in the world) and numerous smaller peripheral islands. Following the prehistoric breakup of the supercontinent Gondwana, Madagascar split from the Indian subcontinent around 88 million years ago, allowing native plants and animals to evolve in relative isolation. Consequently, Madagascar is a biodiversity hotspot; over 90% of its wildlife is endemic.",inline=False)
  embed.add_field(name="Capital",value="Antananarivo",inline=False)
  embed.add_field(name="Flag",value="<:flag_mg:968786126292803625>",inline=False)
  embed.add_field(name="Population",value="28.42 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$45.94 billion",inline=False)
  embed.add_field(name="Currency",value="Ariary",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+261",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Malawi(ctx):
  embed=discord.Embed(title="Malawi",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Malawi, officially the Republic of Malawi, is a landlocked country in Southeastern Africa that was formerly known as Nyasaland. It is bordered by Zambia to the west, Tanzania to the north and northeast, and Mozambique to the east, south and southwest. Malawi spans over 118,484 sq km (45,747 sq mi) and has an estimated population of 19,431,566 (as of January 2021). Malawi's capital (and largest city) is Lilongwe. Its second-largest is Blantyre, its third-largest is Mzuzu and its fourth-largest is its former capital, Zomba. The name Malawi comes from the Maravi, an old name for the Chewa people who inhabit the area. The country is nicknamed The Warm Heart of Africa because of the friendliness of its people.",inline=False)
  embed.add_field(name="Capital",value="Lilongwe",inline=False)
  embed.add_field(name="Flag",value="<:flag_mw:968787802043084840>",inline=False)
  embed.add_field(name="Population",value="19.12 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$30.44 billion",inline=False)
  embed.add_field(name="Currency",value="Malawian kwacha",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+265",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Malaysia(ctx):
  embed=discord.Embed(title="Malaysia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Malaysia, is a country in Southeast Asia. The federal constitutional monarchy consists of thirteen states and three federal territories, separated by the South China Sea into two regions, Peninsular Malaysia and Borneo's East Malaysia. Peninsular Malaysia shares a land and maritime border with Thailand and maritime borders with Singapore, Vietnam, and Indonesia. East Malaysia shares land and maritime borders with Brunei and Indonesia and a maritime border with the Philippines and Vietnam. Kuala Lumpur is the national capital, largest city and the seat of the legislative branch of the federal government. The nearby planned capital of Putrajaya is the administrative capital, which represents the seat of both the executive branch (Cabinet, federal ministries and agencies) and the judicial branch of the federal government.",inline=False)
  embed.add_field(name="Capital",value="Kuala Lumpur",inline=False)
  embed.add_field(name="Flag",value="<:flag_my:968789175681843200>",inline=False)
  embed.add_field(name="Population",value="32.73 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$415.37 billion",inline=False)
  embed.add_field(name="Currency",value="Ringgit",inline=False)
  embed.add_field(name="Time Zone",value="UTC +8",inline=False)
  embed.add_field(name="Dialing Code",value="+60",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Maldives(ctx):
  embed=discord.Embed(title="Maldives",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Maldives, officially the Republic of Maldives, is an archipelagic country in the Indian subcontinent of Asia, situated in the Indian Ocean. It lies southwest of Sri Lanka and India, about 750 kilometres (470 miles; 400 nautical miles) from the Asian continent's mainland. The chain of 26 atolls stretches from Ihavandhippolhu Atoll in the north to Addu Atoll in the south (across the Equator).",inline=False)
  embed.add_field(name="Capital",value="Male",inline=False)
  embed.add_field(name="Flag",value="<:flag_mv:968789896879833098>",inline=False)
  embed.add_field(name="Population",value="579,330",inline=False)
  embed.add_field(name="GDP (PPP)",value="$8.97 billion",inline=False)
  embed.add_field(name="Currency",value="Maldivian rufiyya",inline=False)
  embed.add_field(name="Time Zone",value="UTC +5",inline=False)
  embed.add_field(name="Dialing Code",value="+960",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Mali(ctx):
  embed=discord.Embed(title="Mali",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Mali, officially the Republic of Mali, is a landlocked country in West Africa. Mali is the eighth-largest country in Africa, with an area of over 1,240,000 square kilometres (480,000 sq mi). The population of Mali is 19.1 million. 67% of its population was estimated to be under the age of 25 in 2017. Its capital and largest city is Bamako. The sovereign state of Mali consists of eight regions and its borders on the north reach deep into the middle of the Sahara Desert. The country's southern part is in the Sudanian savanna, where the majority of inhabitants live, and both the Niger and Senegal rivers pass through. The country's economy centres on agriculture and mining. One of Mali's most prominent natural resources is gold, and the country is the third largest producer of gold on the African continent. It also exports salt.",inline=False)
  embed.add_field(name="Capital",value="Bamako",inline=False)
  embed.add_field(name="Flag",value="<:flag_ml:968790679981551626>",inline=False)
  embed.add_field(name="Population",value="20.25 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$44.32 billion",inline=False)
  embed.add_field(name="Currency",value="West African CFA franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC",inline=False)
  embed.add_field(name="Dialing Code",value="+223",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Malta(ctx):
  embed=discord.Embed(title="Malta",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Malta, officially known as the Republic of Malta (Maltese: Repubblika ta' Malta [rɛˈpʊbːlɪkɐ tɐ ˈmɐltɐ]), is an island country in the European Union consisting of an archipelago in the Mediterranean Sea, and considered part of Southern Europe. It lies 80 km (50 mi) south of Sicily (Italy), 284 km (176 mi) east of Tunisia, and 333 km (207 mi) north of Libya. The official languages are Maltese and English, and 66% of the current Maltese population is at least conversational in the Italian language.",inline=False)
  embed.add_field(name="Capital",value="Valletta",inline=False)
  embed.add_field(name="Flag",value="<:flag_mt:968791278185766922>",inline=False)
  embed.add_field(name="Population",value="516,100",inline=False)
  embed.add_field(name="GDP (PPP)",value="$22.80 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+356",inline=False)
  await ctx.send(embed=embed)

@client.command()
async def MarshallIslands(ctx):
  embed=discord.Embed(title="Marshall Islands",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="The Marshall Islands, officially the Republic of the Marshall Islands (Marshallese: Aolepān Aorōkin Ṃajeḷ), is an independent island country near the Equator in the Pacific Ocean, slightly west of the International Date Line. Geographically, the country is part of the larger island group of Micronesia. The country's population of 58,413 people (at the 2018 World Bank Census) is spread out over five islands and 29 coral atolls, comprising 1,156 individual islands and islets. The capital and largest city is Majuro. It has the largest portion of its territory composed of water of any sovereign state, at 97.87%. The islands share maritime boundaries with Wake Island to the north, Kiribati to the southeast, Nauru to the south, and Federated States of Micronesia to the west. About 52.3% of Marshall Islanders (27,797 at the 2011 Census) live on Majuro. In 2016, 73.3% of the population were defined as being urban. The UN also indicates a population density of 760 inhabitants per square mile (295/km2), and its projected 2020 population is 59,190.",inline=False)
  embed.add_field(name="Capital",value="Majuro",inline=False)
  embed.add_field(name="Flag",value="<:flag_mh:969145843762462752>",inline=False)
  embed.add_field(name="Population",value="58,413",inline=False)
  embed.add_field(name="GDP (PPP)",value="$215 million",inline=False)
  embed.add_field(name="Currency",value="United States dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +12",inline=False)
  embed.add_field(name="Dialing Code",value="+962",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Mauritania(ctx):
  embed=discord.Embed(title="Mauritania",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Mauritania, officially the Islamic Republic of Mauritania (Arabic: الجمهورية الإسلامية الموريتانية), is a sovereign state in Northwest Africa. It is bordered by the Atlantic Ocean to the west, Western Sahara to the north and northwest, Algeria to the northeast, Mali to the east and southeast, and Senegal to the southwest. Mauritania is the eleventh largest country in Africa, and 90 percent of its territory is situated in the Sahara. Most of its population of 4.4 million lives in the temperate south of the country, with roughly one third concentrated in the capital and largest city, Nouakchott, located on the Atlantic coast. ",inline=False)
  embed.add_field(name="Capital",value="Nouakchott",inline=False)
  embed.add_field(name="Flag",value="<:flag_mr:969147380035379250>",inline=False)
  embed.add_field(name="Population",value="4.4 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$18.11 billion",inline=False)
  embed.add_field(name="Currency",value="Ouguiya",inline=False)
  embed.add_field(name="Time Zone",value="UTC",inline=False)
  embed.add_field(name="Dialing Code",value="+222",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Mauritius(ctx):
  embed=discord.Embed(title="Mauritius",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Mauritius, officially the Republic of Mauritius, is an island nation in the Indian Ocean about 2,000 kilometres (1,200 mi) off the southeast coast of the African continent, east of Madagascar. It includes the main island (also called Mauritius), as well as Rodrigues, Agaléga and St. Brandon. The islands of Mauritius and Rodrigues, along with nearby Réunion (a French overseas department), are part of the Mascarene Islands. The capital and largest city, Port Louis, is located in Mauritius, where most of the population is concentrated. The country spans 2,040 square kilometres (790 sq mi) and has an exclusive economic zone covering 2.3 million square kilometres.",inline=False)
  embed.add_field(name="Capital",value="Port Louis",inline=False)
  embed.add_field(name="Flag",value="<:flag_mu:969148192841146399>",inline=False)
  embed.add_field(name="Population",value="1.26 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$31.7 billion",inline=False)
  embed.add_field(name="Currency",value="Mauritian rupee",inline=False)
  embed.add_field(name="Time Zone",value="UTC +4",inline=False)
  embed.add_field(name="Dialing Code",value="+230",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Mexico(ctx):
  embed=discord.Embed(title="Mexico",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Mexico, officially the United Mexican States, is a country in the southern portion of North America. It is bordered to the north by the United States; to the south and west by the Pacific Ocean; to the southeast by Guatemala, Belize, and the Caribbean Sea; and to the east by the Gulf of Mexico. Mexico covers 1,972,550 square kilometers (761,610 sq mi), making it the world's 13th-largest country by area; with approximately 126,014,024 inhabitants, it is the 10th-most-populous country and has the most Spanish-speakers. Mexico is organized as a federation comprising 31 states and Mexico City, its capital and largest metropolis. Other major urban areas include Guadalajara, Monterrey, Puebla, Toluca, Tijuana, Ciudad Juárez, and León.",inline=False)
  embed.add_field(name="Capital",value="Mexico City",inline=False)
  embed.add_field(name="Flag",value="<:flag_mx:969151098860486676>",inline=False)
  embed.add_field(name="Population",value="126.01 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.32 trillion",inline=False)
  embed.add_field(name="Currency",value="Mexican peso",inline=False)
  embed.add_field(name="Time Zone",value="UTC -8 to -5 or UTC -7 to -5",inline=False)
  embed.add_field(name="Dialing Code",value="+52",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Micronesia(ctx):
  embed=discord.Embed(title="Micronesia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="The Federated States of Micronesia, or simply Micronesia, is an island country in Oceania. It consists of four states – from west to east, Yap, Chuuk, Pohnpei and Kosrae – that are spread across the western Pacific. Together, the states comprise around 607 islands (a combined land area of approximately 702 sq km or 271 sq mi) that cover a longitudinal distance of almost 2,700 km (1,678 mi) just north of the equator. They lie northeast of Indonesia and Papua New Guinea, south of Guam and the Marianas, west of Nauru and the Marshall Islands, east of Palau and the Philippines, about 2,900 km (1,802 mi) north of eastern Australia, 3,400 km (2,133 mi) southeast of Japan, and some 4,000 km (2,485 mi) southwest of the main islands of the Hawaiian Islands.",inline=False)
  embed.add_field(name="Capital",value="Palikir",inline=False)
  embed.add_field(name="Flag",value="<:flag_fm:969152369176760320>",inline=False)
  embed.add_field(name="Population",value="104,468",inline=False)
  embed.add_field(name="GDP (PPP)",value="$367 million",inline=False)
  embed.add_field(name="Currency",value="United States dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +10 or UTC +11",inline=False)
  embed.add_field(name="Dialing Code",value="+691",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Monaco(ctx):
  embed=discord.Embed(title="Monaco",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Monaco, officially the Principality of Monaco (French: Principauté de Monaco; Ligurian: Prinçipatu de Múnegu), is a sovereign city-state and microstate on the French Riviera a few kilometres west of the Italian region of Liguria, in Western Europe, on the Mediterranean Sea. It is bordered by France to the north, east and west. The principality is home to 38,682 residents, of whom 9,486 are Monégasque nationals; it is widely recognised as one of the most expensive and wealthiest places in the world. The official language of the principality is French. In addition, Monégasque (a dialect of Ligurian), Italian and English are spoken and understood by many residents.",inline=False)
  embed.add_field(name="Capital",value="Monaco",inline=False)
  embed.add_field(name="Flag",value="<:flag_mc:969161011175260220>",inline=False)
  embed.add_field(name="Population",value="38,300",inline=False)
  embed.add_field(name="GDP (PPP)",value="$7.67 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+377",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Mongolia(ctx):
  embed=discord.Embed(title="Mongolia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Mongolia, is a landlocked country in East Asia, bordered by Russia to the north and China to the south. It covers an area of 1,564,116 square kilometres (603,909 square miles), with a population of just 3.3 million, making it the world's most sparsely populated sovereign nation. Mongolia is the world's largest landlocked country that does not border a closed sea, and much of its area is covered by grassy steppe, with mountains to the north and west and the Gobi Desert to the south. Ulaanbaatar, the capital and largest city, is home to roughly half of the country's population.",inline=False)
  embed.add_field(name="Capital",value="Ulaanbaatar",inline=False)
  embed.add_field(name="Flag",value="<:flag_mn:969162265179873280>",inline=False)
  embed.add_field(name="Population",value="3.53 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$47 billion",inline=False)
  embed.add_field(name="Currency",value="Togrog",inline=False)
  embed.add_field(name="Time Zone",value="UTC +7 or UTC +8",inline=False)
  embed.add_field(name="Dialing Code",value="+976",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Montenegro(ctx):
  embed=discord.Embed(title="Montenegro",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Mongolia, is a landlocked country in East Asia, bordered by Russia to the north and China to the south. It covers an area of 1,564,116 square kilometres (603,909 square miles), with a population of just 3.3 million, making it the world's most sparsely populated sovereign nation. Mongolia is the world's largest landlocked country that does not border a closed sea, and much of its area is covered by grassy steppe, with mountains to the north and west and the Gobi Desert to the south. Ulaanbaatar, the capital and largest city, is home to roughly half of the country's population.",inline=False)
  embed.add_field(name="Capital",value="Podgorica",inline=False)
  embed.add_field(name="Flag",value="<:flag_me:969163530664308746>",inline=False)
  embed.add_field(name="Population",value="620,739",inline=False)
  embed.add_field(name="GDP (PPP)",value="$11.99 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+382",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Morocco(ctx):
  embed=discord.Embed(title="Morocco",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Morocco, officially the Kingdom of Morocco, is the northwesternmost country in the Maghreb region of North Africa. It overlooks the Mediterranean Sea to the north and the Atlantic Ocean to the west, and has land borders with Algeria to the east, and the disputed territory of Western Sahara to the south. Morocco also claims the Spanish exclaves of Ceuta, Melilla and Peñón de Vélez de la Gomera, and several small Spanish-controlled islands off its coast. It spans an area of 446,300 sq km (172,300 sq mi) or 710,850 sq km (274,460 sq mi), with a population of roughly 37 million. Its official and predominant religion is Islam, and the official languages are Arabic and Berber; the Moroccan dialect of Arabic and French are also widely spoken. Moroccan identity and culture is a vibrant mix of Berber, Arab, and European cultures. Its capital is Rabat, while its largest city is Casablanca.",inline=False)
  embed.add_field(name="Capital",value="Rabat",inline=False)
  embed.add_field(name="Flag",value="<:flag_ma:969166596188798977>",inline=False)
  embed.add_field(name="Population",value="37.11 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$332.35 billion",inline=False)
  embed.add_field(name="Currency",value="Moroccan dirham",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC",inline=False)
  embed.add_field(name="Dialing Code",value="+212",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Mozambique(ctx):
  embed=discord.Embed(title="Mozambique",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Mozambique, officially the Republic of Mozambique (Portuguese: Moçambique or República de Moçambique, Portuguese pronunciation: [ʁɛˈpuβlikɐ ðɨ musɐ̃ˈbikɨ]; Chichewa: Mozambiki; Swahili: Msumbiji; Tsonga: Muzambhiki), is a country located in Southeastern Africa bordered by the Indian Ocean to the east, Tanzania to the north, Malawi and Zambia to the northwest, Zimbabwe to the west, and Eswatini (Swaziland) and South Africa to the southwest. The sovereign state is separated from the Comoros, Mayotte and Madagascar by the Mozambique Channel to the east. The capital and largest city of Mozambique is Maputo.",inline=False)
  embed.add_field(name="Capital",value="Maputo",inline=False)
  embed.add_field(name="Flag",value="<:flag_mz:969167893482856458>",inline=False)
  embed.add_field(name="Population",value="30.06 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$43.26 billion",inline=False)
  embed.add_field(name="Currency",value="Metical",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+258",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Myanmar(ctx):
  embed=discord.Embed(title="Myanmar",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Myanmar, officially the Republic of the Union of Myanmar (Burmese: ပြည်ထောင်စု သမ္မတ မြန်မာနိုင်ငံတော်‌, [pjìdàuɴzṵ θàɴmədaa̰ mjəmà nàiɴŋàɴdɔ̀]), also called Burma, is a country in Southeast Asia. It is the largest country in Mainland Southeast Asia, and has a population of about 54 million as of 2017. Myanmar is bordered by Bangladesh and India to its northwest, China to its northeast, Laos and Thailand to its east and southeast, and the Andaman Sea and the Bay of Bengal to its south and southwest. The country's capital city is Naypyidaw, and its largest city is Yangon.",inline=False)
  embed.add_field(name="Capital",value="Yangon",inline=False)
  embed.add_field(name="Flag",value="<:flag_mm:969168402075750430>",inline=False)
  embed.add_field(name="Population",value="53.58 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$243.42 billion",inline=False)
  embed.add_field(name="Currency",value="Kyat",inline=False)
  embed.add_field(name="Time Zone",value="UTC +6:30",inline=False)
  embed.add_field(name="Dialing Code",value="+95",inline=False)
  await ctx.send(embed=embed)


#Countries starting with N
@client.command()
async def Namibia(ctx):
  embed=discord.Embed(title="Namibia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Namibia, officially the Republic of Namibia, is a country in Southern Africa. Its western border is the Atlantic Ocean. It shares land borders with Zambia and Angola to the north, Botswana to the east and South Africa to the south and east. Although it does not border Zimbabwe, less than 200 metres (660 feet) of the Botswanan right bank of the Zambezi River separates the two countries. Namibia gained independence from South Africa on 21 March 1990, following the Namibian War of Independence. Its capital and largest city is Windhoek. Namibia is a member state of the United Nations (UN), the Southern African Development Community (SADC), the African Union (AU) and the Commonwealth of Nations.",inline=False)
  embed.add_field(name="Capital",value="Windhoek",inline=False)
  embed.add_field(name="Flag",value="<:flag_na:969169756336824340>",inline=False)
  embed.add_field(name="Population",value="2.55 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$26.64 billion",inline=False)
  embed.add_field(name="Currency",value="Namibian dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+264",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Nauru(ctx):
  embed=discord.Embed(title="Namibia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Nauru, officially the Republic of Nauru (Nauruan: Repubrikin Naoero) and formerly known as Pleasant Island, is an island country and microstate in Oceania, in the Central Pacific. Its nearest neighbour is Banaba Island in Kiribati, 300 km (190 mi) to the east. It further lies northwest of Tuvalu, 1,300 km (810 mi) northeast of Solomon Islands, east-northeast of Papua New Guinea, southeast of the Federated States of Micronesia and south of the Marshall Islands. With only a 21 sq km (8.1 sq mi) area, Nauru is the third-smallest country in the world behind Vatican City and Monaco, making it the smallest republic as well as the smallest island nation. Its population of about 10,000 is the world's second-smallest (not including colonies or overseas territories), after Vatican City.",inline=False)
  embed.add_field(name="Capital",value="Yaren",inline=False)
  embed.add_field(name="Flag",value="<:flag_nr:969170708745846824>",inline=False)
  embed.add_field(name="Population",value="10,834",inline=False)
  embed.add_field(name="GDP (PPP)",value="$132 million",inline=False)
  embed.add_field(name="Currency",value="Australian dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +12",inline=False)
  embed.add_field(name="Dialing Code",value="+674",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Nepal(ctx):
  embed=discord.Embed(title="Nepal",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Nepal, officially the Federal Democratic Republic of Nepal (Nepali: सङ्घीय लोकतान्त्रिक गणतन्त्र नेपाल), is a landlocked country in South Asia. It is mainly situated in the Himalayas, but also includes parts of the Indo-Gangetic Plain, bordering Tibet of China to the north, and India in the south, east, and west, while it is narrowly separated from Bangladesh by the Siliguri Corridor, and from Bhutan by the Indian state of Sikkim. Nepal has a diverse geography, including fertile plains, subalpine forested hills, and eight of the world's ten tallest mountains, including Mount Everest, the highest point on Earth. Nepal is a multi-ethnic, multi-lingual, multi-religious and multi-cultural state, with Nepali as the official language. Kathmandu is the nation's capital and the largest city.",inline=False)
  embed.add_field(name="Capital",value="Kathmandu",inline=False)
  embed.add_field(name="Flag",value="<:flag_np:969171307977654302>",inline=False)
  embed.add_field(name="Population",value="28.09 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$122.62 billion",inline=False)
  embed.add_field(name="Currency",value="Nepalese rupee",inline=False)
  embed.add_field(name="Time Zone",value="UTC +5:45",inline=False)
  embed.add_field(name="Dialing Code",value="+977",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Netherlands(ctx):
  embed=discord.Embed(title="Netherlands",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="The Kingdom of the Netherlands, commonly known as simply the Netherlands, is a sovereign state and constitutional monarchy with 98% of its territory and population in Western Europe and with several small West Indian island territories in the Caribbean (in the Leeward Islands and Leeward Antilles groups). ",inline=False)
  embed.add_field(name="Capital",value="Amsterdam",inline=False)
  embed.add_field(name="Flag",value="<:flag_nl:969172377520992366>",inline=False)
  embed.add_field(name="Population",value="17.73 million",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1",inline=False)
  embed.add_field(name="Dialing Code",value="+31",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def NewZealand(ctx):
  embed=discord.Embed(title="New Zealand",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="New Zealand is an island country in the southwestern Pacific Ocean. It consists of two main landmasses—the North Island (Te Ika-a-Māui) and the South Island (Te Waipounamu)—and over 700 smaller islands. It is the sixth-largest island country, covering a total area of 268,021 square kilometres (103,500 sq mi). New Zealand is about 2,000 kilometres (1,200 mi) east of Australia across the Tasman Sea and 1,000 kilometres (600 mi) south of the islands of New Caledonia, Fiji, and Tonga. The country's varied topography and sharp mountain peaks, including the Southern Alps, owe much to tectonic uplift and volcanic eruptions. New Zealand's capital city is Wellington, and its most populous city is Auckland.",inline=False)
  embed.add_field(name="Capital",value="Wellington",inline=False)
  embed.add_field(name="Flag",value="<:flag_nz:969173970656067595>",inline=False)
  embed.add_field(name="Population",value="5.13 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$222.56 billion",inline=False)
  embed.add_field(name="Currency",value="New Zealand dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +12 to UTC +13",inline=False)
  embed.add_field(name="Dialing Code",value="+64",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Nicaragua(ctx):
  embed=discord.Embed(title="Nicaragua",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Nicaragua, officially the Republic of Nicaragua (Spanish: República de Nicaragua), is the largest country in the Central American isthmus, bordered by Honduras to the northwest, the Caribbean to the east, Costa Rica to the south, and the Pacific Ocean to the southwest. Managua is the country's capital and largest city and is also the third-largest city in Central America, behind Tegucigalpa and Guatemala City. The multi-ethnic population of six million includes people of mestizo, indigenous, European and African heritage. The main language is Spanish. Indigenous tribes on the Mosquito Coast speak their own languages and English.",inline=False)
  embed.add_field(name="Capital",value="Managua",inline=False)
  embed.add_field(name="Flag",value="<:flag_ni:969174834259042314>",inline=False)
  embed.add_field(name="Population",value="6.48 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$35.75 billion",inline=False)
  embed.add_field(name="Currency",value="Corodoba",inline=False)
  embed.add_field(name="Time Zone",value="UTC -6",inline=False)
  embed.add_field(name="Dialing Code",value="+505",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Niger(ctx):
  embed=discord.Embed(title="Niger",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Niger, officially the Republic of the Niger, (Hausa: Jamhuriyar Nijar, Zarma/Songhai: Nigér Laabo, Tamajaq: ⵜⴰⴶⴷⵓⴷⴰ ⵏ ⵏⵉⵌⵢⵔ, Arabic: جمهورية النيجر) is a landlocked country in West Africa named after the Niger River. Niger is a unitary state bordered by Libya to the northeast, Chad to the east, Nigeria to the south, Benin and Burkina Faso to the southwest, Mali to the west, and Algeria to the northwest. Niger covers a land area of almost 1,270,000 sq km (490,000 sq mi), making it the second-largest landlocked country in West Africa, after Chad. Over 80% of its land area lies in the Sahara Desert. The country's predominantly Muslim population of about 22 million live mostly in clusters in the far south and west of the country. The capital and largest city is Niamey, located in Niger's southwest corner.",inline=False)
  embed.add_field(name="Capital",value="Niamey",inline=False)
  embed.add_field(name="Flag",value="<:flag_ne:969175242633269349>",inline=False)
  embed.add_field(name="Population",value="24.11 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$23.47 billion",inline=False)
  embed.add_field(name="Currency",value="West African CFA franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1",inline=False)
  embed.add_field(name="Dialing Code",value="+227",inline=False)
  await ctx.send(embed=embed)

@client.command()
async def Nigeria(ctx):
  embed=discord.Embed(title="Niger",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Nigeria, officially the Federal Republic of Nigeria, is a country in West Africa. It is the most populous country in Africa. It is geographically situated between the Sahel to the north and the Gulf of Guinea to the south in the Atlantic Ocean. It covers an area of 923,769 square kilometres (356,669 sq mi), with a population of over 211 million. Nigeria borders Niger in the north, Chad in the northeast, Cameroon in the east, and Benin in the west. Nigeria is a federal republic comprising 36 states and the Federal Capital Territory, where the capital, Abuja, is located. The largest city in Nigeria is Lagos, one of the largest metropolitan areas in the world and the second-largest in Africa.",inline=False)
  embed.add_field(name="Capital",value="Abuja",inline=False)
  embed.add_field(name="Flag",value="<:flag_ng:969176170765627442>",inline=False)
  embed.add_field(name="Population",value="211.40 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.23 trillion",inline=False)
  embed.add_field(name="Currency",value="Naira",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1",inline=False)
  embed.add_field(name="Dialing Code",value="+234",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def NorthernMacedonia(ctx):
  embed=discord.Embed(title="Niger",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Northern Macedonia, officially the Republic of North Macedonia, is a country in Southeast Europe. It gained independence in 1991 as one of the successor states of Yugoslavia. North Macedonia is a landlocked country bordering Kosovo to the northwest, Serbia to the north, Bulgaria to the east, Greece to the south, and Albania to the west. It constitutes approximately the northern third of the larger geographical region of Macedonia. Skopje, the capital and largest city, is home to a quarter of the country's 1.83 million population. The majority of the residents are ethnic Macedonians, a South Slavic people. Albanians form a significant minority at around 25%, followed by Turks, Romani, Serbs, Bosniaks, Aromanians and a few other minorities.",inline=False)
  embed.add_field(name="Capital",value="Skopje",inline=False)
  embed.add_field(name="Flag",value="<:flag_mk:969176581455118346>",inline=False)
  embed.add_field(name="Population",value="1.83 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$33.82 billion",inline=False)
  embed.add_field(name="Currency",value="Macedonian denar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+389",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Norway(ctx):
  embed=discord.Embed(title="Norway",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Norway, officially the Kingdom of Norway, is a Nordic country in Northern Europe, the mainland territory of which comprises the western and northernmost portion of the Scandinavian Peninsula. The remote Arctic island of Jan Mayen and the archipelago of Svalbard also form part of Norway. Bouvet Island, located in the Subantarctic, is a dependency of Norway; it also lays claims to the Antarctic territories of Peter I Island and Queen Maud Land. The capital and largest city in Norway is Oslo.",inline=False)
  embed.add_field(name="Capital",value="Oslo",inline=False)
  embed.add_field(name="Flag",value="<:flag_no:969177529422331934>",inline=False)
  embed.add_field(name="Population",value="5.42 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$350 billion",inline=False)
  embed.add_field(name="Currency",value="Norwegian krone",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+47",inline=False)
  await ctx.send(embed=embed)



#Countries starting with O
@client.command()
async def Oman(ctx):
  embed=discord.Embed(title="Oman",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Oman, officially the Sultanate of Oman (Arabic: سلْطنةُ عُمان Salṭanat(u) ʻUmān), is a country in Western Asia. It is situated on the southeastern coast of the Arabian Peninsula, and spans the mouth of the Persian Gulf. Oman shares land borders with Saudi Arabia, the United Arab Emirates, and Yemen; while sharing maritime borders with Iran and Pakistan. The coast is formed by the Arabian Sea on the southeast, and the Gulf of Oman on the northeast. The Madha and Musandam exclaves are surrounded by the United Arab Emirates on their land borders, with the Strait of Hormuz (which it shares with Iran) and the Gulf of Oman forming Musandam's coastal boundaries. Muscat is the nation's capital and largest city.",inline=False)
  embed.add_field(name="Capital",value="Muscat",inline=False)
  embed.add_field(name="Flag",value="<:flag_om:969179862399090738>",inline=False)
  embed.add_field(name="Population",value="4.82 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$165.94 billion",inline=False)
  embed.add_field(name="Currency",value="Omani rial",inline=False)
  embed.add_field(name="Time Zone",value="UTC +4",inline=False)
  embed.add_field(name="Dialing Code",value="+968",inline=False)
  await ctx.send(embed=embed)



#Countries Starting with P
@client.command()
async def Pakistan(ctx):
  embed=discord.Embed(title="Pakistan",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Pakistan, officially the Islamic Republic of Pakistan, is a country in South Asia. It is the world's fifth-most populous country, with a population of almost 227 million, and has the world's second-largest Muslim population. Pakistan is the 33rd-largest country by area, spanning 881,913 square kilometres (340,509 square miles). It has a 1,046-kilometre (650-mile) coastline along the Arabian Sea and Gulf of Oman in the south, and is bordered by India to the east, Afghanistan to the west, Iran to the southwest, and China to the northeast. It is separated narrowly from Tajikistan by Afghanistan's Wakhan Corridor in the north, and also shares a maritime border with Oman.",inline=False)
  embed.add_field(name="Capital",value="Islamabad",inline=False)
  embed.add_field(name="Flag",value="<:flag_pk:969180766355460116>",inline=False)
  embed.add_field(name="Population",value="226.99 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.33 trillion",inline=False)
  embed.add_field(name="Currency",value="Pakistan rupee",inline=False)
  embed.add_field(name="Time Zone",value="UTC +5",inline=False)
  embed.add_field(name="Dialing Code",value="+92",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Palau(ctx):
  embed=discord.Embed(title="Palau",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Palau, officially the Republic of Palau (Palauan: Beluu er a Belau) and historically Belau, Palaos or Pelew, is an island country in the western Pacific. The nation has approximately 340 islands and connects the western chain of the Caroline Islands with parts of the Federated States of Micronesia. It has a total area of 466 square kilometers (180 square miles).",inline=False)
  embed.add_field(name="Capital",value="Ngerulmud",inline=False)
  embed.add_field(name="Flag",value="<:flag_pw:969181279721517056>",inline=False)
  embed.add_field(name="Population",value="17,907",inline=False)
  embed.add_field(name="GDP (PPP)",value="$300 million",inline=False)
  embed.add_field(name="Currency",value="United States dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +9",inline=False)
  embed.add_field(name="Dialing Code",value="+680",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Palestine(ctx):
  embed=discord.Embed(title="Palestine",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Palestine, officially the State of Palestine (دولة فلسطين, Dawlat Filasṭīn), is a de jure sovereign state in Western Asia. It is officially governed by the Palestine Liberation Organization (PLO) and claims the West Bank and the Gaza Strip. However, its claimed territory has been occupied by Israel since the Six-Day War of 1967; the West Bank is currently split into 165 Palestinian islands under partial Palestinian National Authority (PNA) civil rule, and 230 Israeli settlements into which Israeli law is pipelined, while Gaza is ruled by Hamas and under a long-term blockade by Egypt and Israel since 2007.",inline=False)
  embed.add_field(name="Capital",value="Jerusalem (limited recognition)",inline=False)
  embed.add_field(name="Flag",value="<:flag_ps:969183465302003752>",inline=False)
  embed.add_field(name="Population",value="5.15 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$26.47 billion",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2 to UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+970",inline=False)
  await ctx.send(embed=embed)





@client.command()
async def Panama(ctx):
  embed=discord.Embed(title="Panama",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Panama, officially the Republic of Panama (Spanish: República de Panamá), is a transcontinental country in Central America and South America, bordered by Costa Rica to the west, Colombia to the southeast, the Caribbean Sea to the north, and the Pacific Ocean to the south. Its capital and largest city is Panama City, whose metropolitan area is home to nearly half the country's 4 million people.",inline=False)
  embed.add_field(name="Capital",value="Panama City",inline=False)
  embed.add_field(name="Flag",value="<:flag_pa:969182489966936064>",inline=False)
  embed.add_field(name="Population",value="4.37 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$128.50 billion",inline=False)
  embed.add_field(name="Currency",value="Balboa and United States dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -5",inline=False)
  embed.add_field(name="Dialing Code",value="+507",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def PapuaNewGuinea(ctx):
  embed=discord.Embed(title="Papua New Guinea",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Papua New Guinea, the Independent State of Papua New Guinea (Tok Pisin: Independen Stet bilong Papua Niugini; Hiri Motu: Independen Stet bilong Papua Niu Gini), is a country in Oceania that comprises the eastern half of the island of New Guinea and its offshore islands in Melanesia (a region of the southwestern Pacific Ocean north of Australia). Its capital, located along its southeastern coast, is Port Moresby. The country is the world's third largest island country with an area of 462,840 sq km (178,700 sq mi).",inline=False)
  embed.add_field(name="Capital",value="Port Moresby",inline=False)
  embed.add_field(name="Flag",value="<:flag_pg:969185527230238740>",inline=False)
  embed.add_field(name="Population",value="8.93 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$32.38 billion",inline=False)
  embed.add_field(name="Currency",value="Kina",inline=False)
  embed.add_field(name="Time Zone",value="UTC +10 or UTC +11",inline=False)
  embed.add_field(name="Dialing Code",value="+675",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Paraguay(ctx):
  embed=discord.Embed(title="Paraguay",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Paraguay, officially the Republic of Paraguay (Spanish: República del Paraguay; Guarani: Tetã Paraguái), is a country in South America. It is bordered by Argentina to the south and southwest, Brazil to the east and northeast, and Bolivia to the northwest. It has a population of 7 million, nearly 3 million of whom live in the capital and largest city of Asunción, and its surrounding metro. Although one of only two landlocked countries in South America (Bolivia is the other), Paraguay has ports on the Paraguay and Paraná rivers that give exit to the Atlantic Ocean, through the Paraná-Paraguay Waterway.",inline=False)
  embed.add_field(name="Capital",value="Asuncion",inline=False)
  embed.add_field(name="Flag",value="<:flag_py:969187438687817808>",inline=False)
  embed.add_field(name="Population",value="7.35 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$101.07 billion",inline=False)
  embed.add_field(name="Currency",value="Guarani",inline=False)
  embed.add_field(name="Time Zone",value="UTC -4 or UTC -3",inline=False)
  embed.add_field(name="Dialing Code",value="+595",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Peru(ctx):
  embed=discord.Embed(title="Peru",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Peru, officially the Republic of Peru (Spanish: República del Perú (help·info)), is a country in western South America. It is bordered in the north by Ecuador and Colombia, in the east by Brazil, in the southeast by Bolivia, in the south by Chile, and in the south and west by the Pacific Ocean. Peru is a megadiverse country with habitats ranging from the arid plains of the Pacific coastal region in the west to the peaks of the Andes mountains extending from the north to the southeast of the country to the tropical Amazon basin rainforest in the east with the Amazon River. Peru has a population of 34 million, and its capital and largest city is Lima. At 1.28 million km2 (0.5 million sq mi), Peru is the 19th largest country in the world, and the third largest in South America.",inline=False)
  embed.add_field(name="Capital",value="Lima",inline=False)
  embed.add_field(name="Flag",value="<:flag_pe:969188507346149437>",inline=False)
  embed.add_field(name="Population",value="34.29 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$385.71 billion",inline=False)
  embed.add_field(name="Currency",value="Sol",inline=False)
  embed.add_field(name="Time Zone",value="UTC -5",inline=False)
  embed.add_field(name="Dialing Code",value="+51",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Philippines(ctx):
  embed=discord.Embed(title="Philippines",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Philippines, officially the Republic of the Philippines (Filipino: Republika ng Pilipinas), is an archipelagic country in Southeast Asia. It is situated in the western Pacific Ocean, and consists of about 7,640 islands, that are broadly categorized under three main geographical divisions from north to south: Luzon, Visayas, and Mindanao. The Philippines is bounded by the West Philippine Sea to the west, the Philippine Sea to the east, and the Celebes Sea to the southwest, and shares maritime borders with Taiwan to the north, Japan to the northeast, Palau to the east and southeast, Indonesia to the south, Malaysia to the southwest, Vietnam to the west, and China to the northwest. The Philippines covers an area of 300,000 sq km (120,000 sq mi) and, as of 2020, had a population of around 109 million people, making it the world's thirteenth-most populous country.",inline=False)
  embed.add_field(name="Capital",value="Manila",inline=False)
  embed.add_field(name="Flag",value="<:flag_ph:969189506949455922>",inline=False)
  embed.add_field(name="Population",value="109.99 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1 trillion",inline=False)
  embed.add_field(name="Currency",value="Philippine peso",inline=False)
  embed.add_field(name="Time Zone",value="UTC +8",inline=False)
  embed.add_field(name="Dialing Code",value="+63",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Poland(ctx):
  embed=discord.Embed(title="Poland",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Poland, officially the Republic of Poland, is a country in Central Europe. It is divided into 16 administrative provinces called voivodeships, covering an area of 312,696 sq km (120,733 sq mi). Poland has a population of over 38 million and is the fifth-most populous member state of the European Union. Warsaw is the nation's capital and largest metropolis. Other major cities include Kraków, Łódź, Wrocław, Poznań, Gdańsk, and Szczecin.",inline=False)
  embed.add_field(name="Capital",value="Warsaw",inline=False)
  embed.add_field(name="Flag",value="<:flag_pl:969190251941736488>",inline=False)
  embed.add_field(name="Population",value="38.17 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.52 trillion",inline=False)
  embed.add_field(name="Currency",value="Zloty",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+48",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Portugal(ctx):
  embed=discord.Embed(title="Portugal",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Portugal, officially the Portuguese Republic (Portuguese: República Portuguesa [ʁɛˈpuβlikɐ puɾtuˈɣezɐ]), is a country whose mainland is located on the Iberian Peninsula of Southwestern Europe, and whose territory also includes the Atlantic archipelagos of the Azores and Madeira. It features the westernmost point in mainland Europe, and its Iberian portion is bordered to the west and south by the Atlantic Ocean and to the north and east by Spain, the sole country to have a land border with Portugal. Its two archipelagos form two autonomous regions with their own regional governments. The official and national language is Portuguese. Lisbon is the capital and largest city.",inline=False)
  embed.add_field(name="Capital",value="Lisbon",inline=False)
  embed.add_field(name="Flag",value="<:flag_pt:969190743027634186>",inline=False)
  embed.add_field(name="Population",value="10.34 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$419.7 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1",inline=False)
  embed.add_field(name="Dialing Code",value="+351",inline=False)
  await ctx.send(embed=embed)



#Countries Starting with Q
@client.command()
async def Qatar(ctx):
  embed=discord.Embed(title="Qatar",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Qatar, officially the State of Qatar, is a country in Western Asia. It occupies the small Qatar Peninsula on the northeastern coast of the Arabian Peninsula, and shares its sole land border with neighbouring Gulf Cooperation Council monarchy Saudi Arabia to the south, with the rest of its territory surrounded by the Persian Gulf. The Gulf of Bahrain, an inlet of the Persian Gulf, separates Qatar from nearby Bahrain. The capital is Doha, home to over 80% of the nation's population.",inline=False)
  embed.add_field(name="Capital",value="Doha",inline=False)
  embed.add_field(name="Flag",value="<:flag_qa:969195715572154408>",inline=False)
  embed.add_field(name="Population",value="2.79 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$315.29 billion",inline=False)
  embed.add_field(name="Currency",value="Qatari riyal",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+974",inline=False)
  await ctx.send(embed=embed)



#Countries Starting with R
@client.command()
async def Romania(ctx):
  embed=discord.Embed(title="Romania",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Romania is a country located at the crossroads of Central, Eastern, and Southeastern Europe. It borders Bulgaria to the south, Ukraine to the north, Hungary to the west, Serbia to the southwest, Moldova to the east, and the Black Sea to the southeast. It has a predominantly temperate-continental climate, and an area of 238,397 sq km (92,046 sq mi), with a population of around 19 million. Romania is the twelfth-largest country in Europe and the sixth-most populous member state of the European Union. Its capital and largest city is Bucharest, and other major urban areas include Iași, Cluj-Napoca, Timișoara, Constanța, Craiova, Brașov, and Galați.",inline=False)
  embed.add_field(name="Capital",value="Bucharest",inline=False)
  embed.add_field(name="Flag",value="<:flag_ro:969197119489593354>",inline=False)
  embed.add_field(name="Population",value="19.18 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$704.35 billion",inline=False)
  embed.add_field(name="Currency",value="Romanian leu",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2 or UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+40",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Russia(ctx):
  embed=discord.Embed(title="Russia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Russia, or the Russian Federation, is a transcontinental country spanning Eastern Europe and Northern Asia. It is the largest country in the world by area, covering over 17,125,191 square kilometres (6,612,073 sq mi), and encompassing one-eighth of Earth's inhabitable landmass. Russia extends across eleven time zones and borders sixteen sovereign nations, the most of any country in the world. It is the ninth-most populous country and the most populous country in Europe, with a population of 145.5 million. The country's capital and largest city is Moscow, the largest city entirely within Europe.",inline=False)
  embed.add_field(name="Capital",value="Moscow",inline=False)
  embed.add_field(name="Flag",value="<:flag_ru:969197681870262272>",inline=False)
  embed.add_field(name="Population",value="145.47 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$4.32 trillion",inline=False)
  embed.add_field(name="Currency",value="Russian ruble",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2 to UTC +12",inline=False)
  embed.add_field(name="Dialing Code",value="+7",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Rwanda(ctx):
  embed=discord.Embed(title="Rwanda",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Rwanda, officially the Republic of Rwanda, is a landlocked country in the Great Rift Valley of Central Africa, where the African Great Lakes region and East Africa converge. Located a few degrees south of the Equator, Rwanda is bordered by Uganda, Tanzania, Burundi, and the Democratic Republic of the Congo. It is highly elevated, giving it the soubriquet land of a thousand hills, with its geography dominated by mountains in the west and savanna to the east, with numerous lakes throughout the country. The climate is temperate to subtropical, with two rainy seasons and two dry seasons each year.",inline=False)
  embed.add_field(name="Capital",value="Kigali",inline=False)
  embed.add_field(name="Flag",value="<:flag_rw:969198622795239454>",inline=False)
  embed.add_field(name="Population",value="12.37 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$33.45 billion",inline=False)
  embed.add_field(name="Currency",value="Rwandan franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+250",inline=False)
  await ctx.send(embed=embed)  

  
#Countries starting with S
@client.command()
async def SaintKittsandNevis(ctx):
  embed=discord.Embed(title="Saint Kitts and Nevis",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Saint Kitts and Nevis, officially the Federation of Saint Christopher and Nevis, is an island country in the West Indies. Located in the Leeward Islands chain of the Lesser Antilles, it is the smallest sovereign state in the Western Hemisphere, in both area and population, as well as the world's smallest sovereign federation. The country is a Commonwealth realm, with Elizabeth II as Queen and head of state. It is the only sovereign federation in the Caribbean.",inline=False)
  embed.add_field(name="Capital",value="Basseterre",inline=False)
  embed.add_field(name="Flag",value="<:flag_kn:969506899793960970>",inline=False)
  embed.add_field(name="Population",value="52,441",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.75 billion",inline=False)
  embed.add_field(name="Currency",value="East Carribean dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -4",inline=False)
  embed.add_field(name="Dialing Code",value="+1 869",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def SaintLucia(ctx):
  embed=discord.Embed(title="Saint Lucia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="is an island country in the West Indies in the eastern Caribbean Sea on the boundary with the Atlantic Ocean. The island was previously called Iyonola, the name given to the island by the native Arawaks, and later Hewanorra, the name given by the native Caribs, two separate Amerindian peoples. Part of the Windward Islands of the Lesser Antilles, it is located north/northeast of the island of Saint Vincent, northwest of Barbados and south of Martinique. It covers a land area of 617 km2 (238 square miles) and reported a population of 165,595 in the 2010 census. St. Lucia's largest city is Castries, its current capital, and its second largest is Soufrière, the first French colonial capital on the island.",inline=False)
  embed.add_field(name="Capital",value="Basseterre",inline=False)
  embed.add_field(name="Flag",value="<:flag_lc:969511116763979806>",inline=False)
  embed.add_field(name="Population",value="184,961",inline=False)
  embed.add_field(name="GDP (PPP)",value="$2.48 billion",inline=False)
  embed.add_field(name="Currency",value="East Carribean dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -4",inline=False)
  embed.add_field(name="Dialing Code",value="+1 758",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def SaintVincentandtheGrenadines(ctx):
  embed=discord.Embed(title="Saint Vincent and the Grenadines",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Saint Vincent and the Grenadines is an island country in the Caribbean. It is located in the southeast Windward Islands of the Lesser Antilles, which lie in the West Indies at the southern end of the eastern border of the Caribbean Sea where the latter meets the Atlantic Ocean.",inline=False)
  embed.add_field(name="Capital",value="Kingstown",inline=False)
  embed.add_field(name="Flag",value="<:flag_vc:969512504260718674>",inline=False)
  embed.add_field(name="Population",value="110,211",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.37 billion",inline=False)
  embed.add_field(name="Currency",value="East Carribean dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -4",inline=False)
  embed.add_field(name="Dialing Code",value="+1 784",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Samoa(ctx):
  embed=discord.Embed(title="Samoa",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Samoa is a Polynesian island country consisting of two main islands (Savai'i and Upolu), two smaller, inhabited islands (Manono and Apolima), and several smaller, uninhabited islands, including the Aleipata Islands (Nu'utele, Nu'ulua, Fanuatapu and Namua). Samoa is located 64 km (40 mi) west of American Samoa, 889 km (552 mi) northeast of Tonga (closest foreign country), 1,152 km (716 mi) northeast of Fiji, 483 km (300 mi) east of Wallis and Futuna, 1,151 km (715 mi) southeast of Tuvalu, 519 km (322 mi) south of Tokelau, 4,190 km (2,600 mi) southwest of Hawaii, and 610 km (380 mi) northwest of Niue. The capital city is Apia. The Lapita people discovered and settled the Samoan Islands around 3,500 years ago.",inline=False)
  embed.add_field(name="Capital",value="Apia",inline=False)
  embed.add_field(name="Flag",value="<:flag_ws:969513334175059999>",inline=False)
  embed.add_field(name="Population",value="202,506",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.18 billion",inline=False)
  embed.add_field(name="Currency",value="Tala",inline=False)
  embed.add_field(name="Time Zone",value="UTC +13",inline=False)
  embed.add_field(name="Dialing Code",value="+685",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def SanMarino(ctx):
  embed=discord.Embed(title="San Marino",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="San Marino, officially the Republic of San Marino (Italian: Repubblica di San Marino; Romagnol: Ripóbblica d' San Marein), also known as the Most Serene Republic of San Marino (Italian: Serenissima Repubblica di San Marino), is a small country (and a European microstate) in Southern Europe enclaved by Italy. Located on the northeastern side of the Apennine Mountains, San Marino covers a land area of just over 61 sq km (24 sq mi), and has a population of 33,562.",inline=False)
  embed.add_field(name="Capital",value="Sao Tome",inline=False)
  embed.add_field(name="Flag",value="<:flag_sm:969514171433639946>",inline=False)
  embed.add_field(name="Population",value="33,600",inline=False)
  embed.add_field(name="GDP (PPP)",value="$2.09 billion",inline=False)
  embed.add_field(name="Currency",value="Dobra",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+378",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def SaoTomeandPrincipe(ctx):
  embed=discord.Embed(title="Sao Tome and Principe",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="officially the Democratic Republic of São Tomé and Príncipe (Portuguese: República Democrática de São Tomé e Príncipe), is an island country in the Gulf of Guinea, off the western equatorial coast of Central Africa. It consists of two archipelagos around the two main islands of São Tomé and Príncipe, about 150 km (93.21 mi) apart and about 250 and 225 km (155 and 140 mi) off the north-western coast of Gabon. With a population of 201,800 (2018 official estimate), São Tomé and Príncipe is the second-smallest and second-least populous African sovereign state after Seychelles.",inline=False)
  embed.add_field(name="Capital",value="San Marino",inline=False)
  embed.add_field(name="Flag",value="<:flag_sm:969514171433639946>",inline=False)
  embed.add_field(name="Population",value="211,028",inline=False)
  embed.add_field(name="GDP (PPP)",value="$685 million",inline=False)
  embed.add_field(name="Currency",value="Dobra",inline=False)
  embed.add_field(name="Time Zone",value="UTC",inline=False)
  embed.add_field(name="Dialing Code",value="+239",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def SaudiArabia(ctx):
  embed=discord.Embed(title="Saudi Arabia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Saudi Arabia, is a country on the Arabian Peninsula in Western Asia. It has a land area of about 2,150,000 sq km (830,000 sq mi), making it the fifth-largest country in Asia, the second-largest in the Arab world, and the largest in Western Asia. It is bordered by the Red Sea to the west; Jordan, Iraq, and Kuwait to the north; the Persian Gulf, Qatar and the United Arab Emirates to the east; Oman to the southeast; and Yemen to the south. Bahrain is an island country off the east coast. The Gulf of Aqaba in the northwest separates Saudi Arabia from Egypt. Saudi Arabia is the only country with a coastline along both the Red Sea and the Persian Gulf, and most of its terrain consists of arid desert, lowland, steppe, and mountains. Its capital and largest city is Riyadh.",inline=False)
  embed.add_field(name="Capital",value="Riyadh",inline=False)
  embed.add_field(name="Flag",value="<:flag_sa:969516323702968340>",inline=False)
  embed.add_field(name="Population",value="34.21 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.87 trillion",inline=False)
  embed.add_field(name="Currency",value="Saudi Riyal",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+966",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Senegal(ctx):
  embed=discord.Embed(title="Senegal",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Senegal, officially the Republic of Senegal is a country in West Africa. It is bordered by Mauritania in the north, Mali to the east, Guinea to the southeast, and Guinea-Bissau to the southwest. It nearly surrounds The Gambia, a country occupying a narrow sliver of land along the banks of the Gambia River, which separates Senegal's southern region of Casamance from the rest of the country. Senegal also shares a maritime border with Cape Verde. Its economic and political capital is Dakar. ",inline=False)
  embed.add_field(name="Capital",value="Dakar",inline=False)
  embed.add_field(name="Flag",value="<:flag_sn:969522949679902720>",inline=False)
  embed.add_field(name="Population",value="15.85 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$66.43 billion",inline=False)
  embed.add_field(name="Currency",value="West African CFA franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC",inline=False)
  embed.add_field(name="Dialing Code",value="+221",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Serbia(ctx):
  embed=discord.Embed(title="Serbia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Serbia, officially the Republic of Serbia (Serbian: Република Србија, Republika Srbija, pronounced [repǔblika sř̩bija], is a landlocked country in Southeast Europe, at the crossroads of the Pannonian Plain and the Balkans. It shares land borders with Hungary to the north, Romania to the northeast, Bulgaria to the southeast, North Macedonia to the south, Croatia and Bosnia and Herzegovina to the west, and Montenegro to the southwest, and claiming a border with Albania through the disputed territory of Kosovo. Serbia with Kosovo has about 8.6 million inhabitants. Its capital Belgrade is also the largest city. ",inline=False)
  embed.add_field(name="Capital",value="Belagrade",inline=False)
  embed.add_field(name="Flag",value="<:flag_rs:969524510363623424>",inline=False)
  embed.add_field(name="Population",value="7.18 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$157.40 billion",inline=False)
  embed.add_field(name="Currency",value="Serbian dinar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+381",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Seychelles(ctx):
  embed=discord.Embed(title="Seychelles",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Seychelles, officially the Republic of Seychelles (French: République des Seychelles; Creole: La Repiblik Sesel), is an archipelagic island country consisting of 115 islands in the Indian Ocean at the eastern edge of the Somali Sea. Its capital and largest city, Victoria, is 1,500 kilometres (800 nautical miles) east of mainland Africa. Nearby island countries and territories include the Comoros, Madagascar, Mauritius, and the French overseas regions of Mayotte and Réunion to the south; and Maldives and the Chagos Archipelago (administered by the United Kingdom as the British Indian Ocean Territory) to the east. It is the least populous sovereign African country, with an estimated 2020 population of 98,462.",inline=False)  
  embed.add_field(name="Capital",value="Victoria",inline=False)
  embed.add_field(name="Flag",value="<:flag_sc:969527460620304415>",inline=False)
  embed.add_field(name="Population",value="99,331",inline=False)
  embed.add_field(name="GDP (PPP)",value="$3.5 billion",inline=False)
  embed.add_field(name="Currency",value="Seychellois rupee",inline=False)
  embed.add_field(name="Time Zone",value="UTC +4",inline=False)
  embed.add_field(name="Dialing Code",value="+248",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def SierraLeone(ctx):
  embed=discord.Embed(title="Sierra Leone",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Sierra Leone, officially the Republic of Sierra Leone, informally Salone, is a country on the southwest coast of West Africa. It is bordered by Liberia to the southeast and Guinea surrounds the northern half of the nation. Sierra Leone has a tropical climate with a diverse environment ranging from savanna to rainforests, a total area of 71,740 sq km (27,699 sq mi) and a population of 7,092,113 as of the 2015 census. The capital and largest city is Freetown. The country is divided into five administrative regions which are subdivided into sixteen districts.",inline=False)  
  embed.add_field(name="Capital",value="Freetown",inline=False)
  embed.add_field(name="Flag",value="<:flag_sl:969528934398050314>",inline=False)
  embed.add_field(name="Population",value="8.05 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$12.17 billion",inline=False)
  embed.add_field(name="Currency",value="Leone",inline=False)
  embed.add_field(name="Time Zone",value="UTC",inline=False)
  embed.add_field(name="Dialing Code",value="+232",inline=False)
  await ctx.send(embed=embed)

@client.command()
async def Singapore(ctx):
  embed=discord.Embed(title="Singapore",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Singapore, officially the Republic of Singapore, is a sovereign island city-state in maritime Southeast Asia. It lies about one degree of latitude (137 kilometres or 85 miles) north of the equator, off the southern tip of the Malay Peninsula, bordering the Strait of Malacca to the west, the Singapore Strait to the south, the South China Sea to the east and the Straits of Johor to the north. The country's territory is composed of one main island, 63 satellite islands and islets, and one outlying islet, the combined area of which has increased by 25% since the country's independence as a result of extensive land reclamation projects.",inline=False)  
  embed.add_field(name="Capital",value="Singapore",inline=False)
  embed.add_field(name="Flag",value="<:flag_sg:969529951021854740>",inline=False)
  embed.add_field(name="Population",value="5.45 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$600.06 billion",inline=False)
  embed.add_field(name="Currency",value="Singapore dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +8",inline=False)
  embed.add_field(name="Dialing Code",value="+65",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Slovakia(ctx):
  embed=discord.Embed(title="Slovakia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Slovakia, officially the Slovak Republic (Slovak: Slovenská republika [ˈslɔʋenskaː ˈrepublika], is a landlocked country in Central Europe. It is bordered by Poland to the north, Ukraine to the east, Hungary to the south, Austria to the southwest, and the Czech Republic to the northwest. Slovakia's mostly mountainous territory spans about 49,000 square kilometres (19,000 sq mi), with a population of over 5.4 million. The capital and largest city is Bratislava, while the second largest city is Košice.",inline=False)  
  embed.add_field(name="Capital",value="Bratislava",inline=False)
  embed.add_field(name="Flag",value="<:flag_sk:969530593849262150>",inline=False)
  embed.add_field(name="Population",value="5.44 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$203.24 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 and UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+421",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Slovenia(ctx):
  embed=discord.Embed(title="Slovenia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Slovenia, officially the Republic of Slovenia (Slovene: Republika Slovenija, abbr.: RS), is a country in Central Europe. It is bordered by Italy to the west, Austria to the north, Hungary to the northeast, Croatia to the southeast, and the Adriatic Sea to the southwest. Slovenia is mostly mountainous and forested, covers 20,271 square kilometres (7,827 sq mi), and has a population of 2.1 million (2,108,708 people). Slovenes constitute over 80% of the country's population. Slovene, a South Slavic language, is the official language.",inline=False)  
  embed.add_field(name="Capital",value="Ljubljana",inline=False)
  embed.add_field(name="Flag",value="<:flag_si:969532014531342356>",inline=False)
  embed.add_field(name="Population",value="2.10 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$97.7 billion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 and UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+386",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def SolomonIslands(ctx):
  embed=discord.Embed(title="Solomon Islands",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Solomon Islands consisting of six major islands and over 900 smaller islands in Oceania, to the east of Papua New Guinea and northwest of Vanuatu. It has a land area of 28,400 square kilometres (11,000 sq mi), and a population of 652,858. Its capital, Honiara, is located on the largest island, Guadalcanal. The country takes its name from the Solomon Islands archipelago, which is a collection of Melanesian islands that also includes the North Solomon Islands (a part of Papua New Guinea), but excludes outlying islands, such as the Santa Cruz Islands and Rennell and Bellona.",inline=False)  
  embed.add_field(name="Capital",value="Honiara",inline=False)
  embed.add_field(name="Flag",value="<:flag_sb:969533532361875480>",inline=False)
  embed.add_field(name="Population",value="652,857",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.47 billion",inline=False)
  embed.add_field(name="Currency",value="Solomon Islands dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +11",inline=False)
  embed.add_field(name="Dialing Code",value="+677",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Somalia(ctx):
  embed=discord.Embed(title="Somalia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Somalia, is a country in the Horn of Africa. The country is bordered by Ethiopia to the west, Djibouti to the northwest, the Gulf of Aden to the north, the Indian Ocean to the east, and Kenya to the southwest. Somalia has the longest coastline on Africa's mainland. Its terrain consists mainly of plateaus, plains, and highlands. Hot conditions prevail year-round, with periodic monsoon winds and irregular rainfall. Somalia has an estimated population of around 15 million, of which over 2 million live in the capital and largest city Mogadishu, and has been described as Africa's most culturally homogeneous country.",inline=False)  
  embed.add_field(name="Capital",value="Mogadishu",inline=False)
  embed.add_field(name="Flag",value="<:flag_so:969534172169371689>",inline=False)
  embed.add_field(name="Population",value="15.89 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$13.32 billion",inline=False)
  embed.add_field(name="Currency",value="Somali shilling",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+252",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def SouthAfrica(ctx):
  embed=discord.Embed(title="South Africa",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="South Africa, officially the Republic of South Africa (RSA), is the southernmost country in Africa. With over 60 million people, the country is the world's 23rd-most populous nation and covers an area of 1,221,037 square kilometres (471,445 square miles). South Africa has three capital cities, with the executive, judicial and legislative branches of government based in Pretoria, Bloemfontein and Cape Town respectively. The largest city is Johannesburg.",inline=False)  
  embed.add_field(name="Capital",value="Pretoria (Executive), Cape Town (Legislative) and Bloemfontein (Judicial)",inline=False)
  embed.add_field(name="Flag",value="<:flag_za:969535408633421874>",inline=False)
  embed.add_field(name="Population",value="60.14 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$924 billion",inline=False)
  embed.add_field(name="Currency",value="South African rand",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+27",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def SouthKorea(ctx):
  embed=discord.Embed(title="South Korea",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="South Korea, officially the Republic of Korea (ROK), is a country in East Asia, constituting the southern part of the Korean Peninsula and sharing a land border with North Korea. Its western border is formed by the Yellow Sea, while its eastern border is defined by the Sea of Japan. South Korea claims to be the sole legitimate government of the entire peninsula and adjacent islands. It has a population of 51 million, of which roughly half live in the Seoul Capital Area, the fifth largest metropolis in the world. Other major cities include Incheon, Busan, and Daegu.",inline=False)  
  embed.add_field(name="Capital",value="Seoul",inline=False)
  embed.add_field(name="Flag",value="<:flag_kr:969535977754361869>",inline=False)
  embed.add_field(name="Population",value="51.70 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$2.43 trillion",inline=False)
  embed.add_field(name="Currency",value="Korean Republic won",inline=False)
  embed.add_field(name="Time Zone",value="UTC +9",inline=False)
  embed.add_field(name="Dialing Code",value="+82",inline=False)
  await ctx.send(embed=embed)  
  
  
  
@client.command()
async def SouthSudan(ctx):
  embed=discord.Embed(title="South Sudan",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="South Sudan, officially known as the Republic of South Sudan, is a landlocked country in Central Africa. It is bordered by Ethiopia, Sudan, Central African Republic, Democratic Republic of the Congo, Uganda and Kenya. Its population was estimated as 12,778,250 in 2019. Juba is the capital and largest city. The nation is sometimes informally referred to as the Nilotic Republic.",inline=False)  
  embed.add_field(name="Capital",value="Juba",inline=False)
  embed.add_field(name="Flag",value="<:flag_ss:969853080990523463>",inline=False)
  embed.add_field(name="Population",value="12.77 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$18.43 billion",inline=False)
  embed.add_field(name="Currency",value="South Sudanese pound",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+211",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Spain(ctx):
  embed=discord.Embed(title="Spain",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Spain or the Kingdom of Spain (Spanish: Reino de España),[a] is a country in southwestern Europe with parts of territory in the Atlantic Ocean and across the Mediterranean Sea. The largest part of Spain is situated on the Iberian Peninsula; its territory also includes the Canary Islands in the Atlantic Ocean, the Balearic Islands in the Mediterranean Sea, the autonomous cities of Ceuta and Melilla, and several minor overseas territories also scattered along the Moroccan coast of the Alboran Sea.[13] The country's mainland is bordered to the south by Gibraltar; to the south and east by the Mediterranean Sea; to the north by France, Andorra and the Bay of Biscay; and to the west by Portugal and the Atlantic Ocean.",inline=False)  
  embed.add_field(name="Capital",value="Madrid",inline=False)
  embed.add_field(name="Flag",value="<:flag_es:969854146842857492>",inline=False)
  embed.add_field(name="Population",value="47.45 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$2.20 trillion",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC to UTC +1 or UTC +1 to UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+34",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def SriLanka(ctx):
  embed=discord.Embed(title="Sri Lanka",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Sri Lanka, formerly known as Ceylon, and officially the Democratic Socialist Republic of Sri Lanka, is an island country in South Asia. It lies in the Indian Ocean, southwest of the Bay of Bengal, and southeast of the Arabian Sea; it is separated from the Indian subcontinent by the Gulf of Mannar and the Palk Strait. Sri Lanka shares a maritime border with India and the Maldives. Sri Jayawardenepura Kotte is its legislative capital, and Colombo is its largest city and financial centre.",inline=False)  
  embed.add_field(name="Capital",value="Colombo",inline=False)
  embed.add_field(name="Flag",value="<:flag_lk:969854897677824090>",inline=False)
  embed.add_field(name="Population",value="22.15 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$84.53 billion",inline=False)
  embed.add_field(name="Currency",value="Sri Lankan rupee",inline=False)
  embed.add_field(name="Time Zone",value="UTC +5:30",inline=False)
  embed.add_field(name="Dialing Code",value="+94",inline=False)
  await ctx.send(embed=embed)

@client.command()
async def Sudan(ctx):
  embed=discord.Embed(title="Sudan",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Sudan,  officially the Republic of the Sudan (Arabic: جمهورية السودان, romanized: Jumhūriyyat as-Sūdān) and also known as North Sudan, is a country in Northeast Africa. It shares borders with the Central African Republic to the southwest, Chad to the west, Egypt to the north, Eritrea to the northeast, Ethiopia to the southeast, Libya to the northwest, South Sudan to the south and the Red Sea. It has a population of 45.70 million people as of 2022[13] and occupies 1,886,068 square kilometres (728,215 square miles), making it Africa's third-largest country by area, and the third-largest by area in the Arab League.",inline=False)  
  embed.add_field(name="Capital",value="Khartoum",inline=False)
  embed.add_field(name="Flag",value="<:flag_sd:969855676740403280>",inline=False)
  embed.add_field(name="Population",value="45.70 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$177.67 billion",inline=False)
  embed.add_field(name="Currency",value="Sudanese pound",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+249",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Suriname(ctx):
  embed=discord.Embed(title="Suriname",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Suriname, officially known as the Republic of Suriname (Dutch: Republiek Suriname [reːpyˌblik ˌsyːriˈnaːmə]), is a country on the northeastern Atlantic coast of South America. It is bordered by the Atlantic Ocean to the north, French Guiana to the east, Guyana to the west, and Brazil to the south. At just under 165,000 square kilometers (64,000 square miles), it is the smallest sovereign state in South America.[note 1] It has a population of approximately 575,990, most of whom live on the country's north coast, in and around its capital and largest city, Paramaribo.",inline=False)  
  embed.add_field(name="Capital",value="Paramaribo",inline=False)
  embed.add_field(name="Flag",value="<:flag_sr:969856306724876328>",inline=False)
  embed.add_field(name="Population",value="575,990",inline=False)
  embed.add_field(name="GDP (PPP)",value="$9.04 billion",inline=False)
  embed.add_field(name="Currency",value="Surinamese dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -3",inline=False)
  embed.add_field(name="Dialing Code",value="+597",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Sweeden(ctx):
  embed=discord.Embed(title="Sweeden",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Sweeden, officially the Kingdom of Sweden (Swedish: Konungariket Sverige [ˈkôːnɵŋaˌriːkɛt ˈsvæ̌rjɛ], is a Nordic country in Northern Europe. It borders Norway to the west and north, Finland to the east, and is connected to Denmark in the southwest by a bridge-tunnel across the Öresund. At 450,295 square kilometres (173,860 sq mi), Sweden is the largest country in Northern Europe, the third-largest country in the European Union, and the fifth largest country in Europe. The capital and largest city is Stockholm.",inline=False)  
  embed.add_field(name="Capital",value="Stockholm",inline=False)
  embed.add_field(name="Flag",value="<:flag_se:969857119903948820>",inline=False)
  embed.add_field(name="Population",value="10.40 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$563.88 billion",inline=False)
  embed.add_field(name="Currency",value="Sweedish krona",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+46",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Switzerland(ctx):
  embed=discord.Embed(title="Switzerland",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Switzerland, officially the Swiss Confederation, is a landlocked country at the confluence of Western, Central and Southern Europe. The country is a federal republic composed of 26 cantons, with federal authorities based in Bern. Switzerland is bordered by Italy to the south, France to the west, Germany to the north and Austria and Liechtenstein to the east. It is geographically divided among the Swiss Plateau, the Alps and the Jura, spanning a total area of 41,285 sq km (15,940 sq mi) and land area of 39,997 sq km (15,443 sq mi). Although the Alps occupy the greater part of the territory, the Swiss population of approximately 8.5 million is concentrated mostly on the plateau, where the largest cities and economic centres are, among them Zürich, Geneva and Basel. These three cities are home to several offices of international organisations such as the WTO, the WHO, the ILO, the headquarters of FIFA, the UN's second-largest office, as well as the main office of the Bank for International Settlements.",inline=False)  
  embed.add_field(name="Capital",value="Bern (de facto)",inline=False)
  embed.add_field(name="Flag",value="<:flag_ch:969858213874913310>",inline=False)
  embed.add_field(name="Population",value="8.57 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$584 billion",inline=False)
  embed.add_field(name="Currency",value="Swiss franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+41",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Syria(ctx):
  embed=discord.Embed(title="Syria",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Syria, officially the Syrian Arab Republic (Arabic: ٱلْجُمْهُورِيَّةُ ٱلْعَرَبِيَّةُ ٱلسُّورِيَّةُ, romanized: al-Jumhūrīyah al-ʻArabīyah as-Sūrīyah), is a country in Western Asia. Syria borders the Mediterranean Sea to the west, Turkey to the north, Iraq to the east and southeast, Jordan to the south, and Israel and Lebanon to the southwest. Cyprus lies to the west across the Mediterranean Sea. A country of fertile plains, high mountains, and deserts, Syria is home to diverse ethnic and religious groups, including the majority Syrian Arabs, Kurds, Turkmens, Assyrians, Armenians, Circassians, and Greeks. Religious groups include Sunnis, Christians, Alawites, Druze, Isma'ilis, Shiites, Salafis, and Yazidis. The capital and largest city of Syria is Damascus.",inline=False)  
  embed.add_field(name="Capital",value="Damascus",inline=False)
  embed.add_field(name="Flag",value="<:flag_sy:969858864688300102>",inline=False)
  embed.add_field(name="Population",value="17.50 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$50.28 billion",inline=False)
  embed.add_field(name="Currency",value="Syrian pound",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2 or UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+963",inline=False)
  await ctx.send(embed=embed)



#Countries Starting with T
@client.command()
async def Taiwan(ctx):
  embed=discord.Embed(title="Taiwan",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Taiwan,  officially the Republic of China (ROC), is a country in East Asia, at the junction of the East and South China Seas in the northwestern Pacific Ocean, with the People's Republic of China (PRC) to the northwest, Japan to the northeast, and the Philippines to the south. The territories controlled by the ROC consist of 168 islands, with a combined area of 36,193 square kilometres (13,974 sq mi). The main island of Taiwan, formerly known as Formosa, has an area of 35,808 square kilometres (13,826 sq mi), with mountain ranges dominating the eastern two-thirds and plains in the western third, where its highly urbanised population is concentrated. The capital, Taipei, forms along with New Taipei City and Keelung the largest metropolitan area of Taiwan. Other major cities include Kaohsiung, Taichung, Tainan, and Taoyuan. With 23.45 million inhabitants, Taiwan is among the most densely populated countries in the world.",inline=False)  
  embed.add_field(name="Capital",value="Taipei",inline=False)
  embed.add_field(name="Flag",value="<:flag_tw:969863016000671744>",inline=False)
  embed.add_field(name="Population",value="23.45 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.40 trillion",inline=False)
  embed.add_field(name="Currency",value="New Taiwan dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +8",inline=False)
  embed.add_field(name="Dialing Code",value="+886",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Tajikistan(ctx):
  embed=discord.Embed(title="Tajikistan",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Tajikistan,  officially the Republic of Tajikistan (Tajik: Ҷумҳурии Тоҷикистон, romanized: Jumhurii Tojikiston), is a landlocked country in Central Asia. It has an area of 143,100 sq km (55,300 sq mi) and an estimated population of 9,537,645 people. Its capital and largest city is Dushanbe. It is bordered by Afghanistan to the south, Uzbekistan to the west, Kyrgyzstan to the north and China to the east. It is separated narrowly from Pakistan by Afghanistan's Wakhan Corridor. The traditional homelands of the Tajik people include present-day Tajikistan as well as parts of Afghanistan and Uzbekistan.",inline=False)  
  embed.add_field(name="Capital",value="Dushanbe",inline=False)
  embed.add_field(name="Flag",value="<:flag_tj:969863791225475072>",inline=False)
  embed.add_field(name="Population",value="9.53 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$30.54 billion",inline=False)
  embed.add_field(name="Currency",value="Somoni",inline=False)
  embed.add_field(name="Time Zone",value="UTC +5",inline=False)
  embed.add_field(name="Dialing Code",value="+992",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Tanzania(ctx):
  embed=discord.Embed(title="Tanzania",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Tanzania, officially the United Republic of Tanzania (Swahili: Jamhuri ya Muungano wa Tanzania), is a country in East Africa within the African Great Lakes region. It borders Uganda to the north; Kenya to the northeast; Comoro Islands and the Indian Ocean to the east; Mozambique and Malawi to the south; Zambia to the southwest; and Rwanda, Burundi, and the Democratic Republic of the Congo to the west. Mount Kilimanjaro, Africa's highest mountain, is in northeastern Tanzania.",inline=False)  
  embed.add_field(name="Capital",value="Dodoma",inline=False)
  embed.add_field(name="Flag",value="<:flag_tz:969864285968805889>",inline=False)
  embed.add_field(name="Population",value="61.19 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$205.48 billion",inline=False)
  embed.add_field(name="Currency",value="Tanzanian shilling",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+255",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Thailand(ctx):
  embed=discord.Embed(title="Thailand",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Thailand, historically known as Siam (/saɪˈæm, ˈsaɪæm/) and officially the Kingdom of Thailand, is a country in Southeast Asia spanning 513,120 square kilometres (198,120 sq mi), with a population of almost 70 million. It is bordered to the north by Myanmar and Laos, to the east by Laos and Cambodia, to the south by the Gulf of Thailand and Malaysia, and to the west by the Andaman Sea and Myanmar. Thailand also shares maritime borders with Vietnam to the southeast, and Indonesia and India to the southwest. Thailand has experienced multiple coups and military dictatorships. Since 2019, Thailand has been nominally a parliamentary constitutional monarchy.",inline=False)  
  embed.add_field(name="Capital",value="Bangkok",inline=False)
  embed.add_field(name="Flag",value="<:flag_th:969865295076393001>",inline=False)
  embed.add_field(name="Population",value="66.17 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.47 trillion",inline=False)
  embed.add_field(name="Currency",value="Baht",inline=False)
  embed.add_field(name="Time Zone",value="UTC +7",inline=False)
  embed.add_field(name="Dialing Code",value="+66",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def TimorLeste(ctx):
  embed=discord.Embed(title="Timor Liste",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Timor Leste, officially the Democratic Republic of Timor-Leste (Portuguese: República Democrática de Timor-Leste, Tetum: Repúblika Demokrátika Timór-Leste) is an island country in Southeast Asia. It comprises the eastern half of the island of Timor, the nearby islands of Atauro and Jaco, and Oecusse, an exclave on the northwestern side of the island surrounded by Indonesian West Timor. Australia is the country's southern neighbour, separated by the Timor Sea. The country's size is 15,007 square kilometres (5,794 sq mi). Dili is its capital. ",inline=False)  
  embed.add_field(name="Capital",value="Dili",inline=False)
  embed.add_field(name="Flag",value="<:flag_tl:969867633103089764>",inline=False)
  embed.add_field(name="Population",value="1.34 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$5.31 billion",inline=False)
  embed.add_field(name="Currency",value="United States dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +9",inline=False)
  embed.add_field(name="Dialing Code",value="+670",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Togo(ctx):
  embed=discord.Embed(title="Togo",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Thailand, historically known as Siam (/saɪˈæm, ˈsaɪæm/) and officially the Kingdom of Thailand, is a country in Southeast Asia spanning 513,120 square kilometres (198,120 sq mi), with a population of almost 70 million. It is bordered to the north by Myanmar and Laos, to the east by Laos and Cambodia, to the south by the Gulf of Thailand and Malaysia, and to the west by the Andaman Sea and Myanmar. Thailand also shares maritime borders with Vietnam to the southeast, and Indonesia and India to the southwest. Thailand has experienced multiple coups and military dictatorships. Since 2019, Thailand has been nominally a parliamentary constitutional monarchy.",inline=False)  
  embed.add_field(name="Capital",value="Lome",inline=False)
  embed.add_field(name="Flag",value="<:flag_tg:969868558869864468>",inline=False)
  embed.add_field(name="Population",value="8.60 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$14.91 billion",inline=False)
  embed.add_field(name="Currency",value="West African CFA franc",inline=False)
  embed.add_field(name="Time Zone",value="UTC",inline=False)
  embed.add_field(name="Dialing Code",value="+228",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Tonga(ctx):
  embed=discord.Embed(title="Tonga",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Tonga, officially named the Kingdom of Tonga (Tongan: Puleʻanga Fakatuʻi ʻo Tonga), is a Polynesian country and also an archipelago consisting of 169 islands, of which 36 are inhabited. The total surface area of the archipelago is about 750 sq km (290 sq mi), scattered over 700,000 sq km (270,000 sq mi) of the southern Pacific Ocean.",inline=False)  
  embed.add_field(name="Capital",value="Nuku'alofa",inline=False)
  embed.add_field(name="Flag",value="<:flag_to:969869284320878632>",inline=False)
  embed.add_field(name="Population",value="100,209",inline=False)
  embed.add_field(name="GDP (PPP)",value="$655 million",inline=False)
  embed.add_field(name="Currency",value="Pa'anga",inline=False)
  embed.add_field(name="Time Zone",value="UTC +13",inline=False)
  embed.add_field(name="Dialing Code",value="+676",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def TrinidadandTobago(ctx):
  embed=discord.Embed(title="Trinidad and Tobago",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Trinidad and Tobago, officially the Republic of Trinidad and Tobago, is the southernmost island country in the Caribbean. It is known for its fossil-fuel wealth. Consisting of the main islands Trinidad and Tobago, and numerous much smaller islands, it is situated 130 kilometres (81 miles) south of Grenada and 11 kilometres (6.8 miles) off the coast of northeastern Venezuela. It shares maritime boundaries with Barbados to the northeast, Grenada to the northwest and Venezuela to the south and west. Trinidad and Tobago is generally considered to be part of the West Indies.",inline=False)  
  embed.add_field(name="Capital",value="Port of Spain",inline=False)
  embed.add_field(name="Flag",value="<:flag_tt:969870317113720853>",inline=False)
  embed.add_field(name="Population",value="1.36 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$45.14 billion",inline=False)
  embed.add_field(name="Currency",value="Trinidad and Tobago dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -4",inline=False)
  embed.add_field(name="Dialing Code",value="+1",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Tunisia(ctx):
  embed=discord.Embed(title="Tunisia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Tunisia, officially the Republic of Tunisia, is the northernmost country in Africa. It is a part of the Maghreb region of North Africa, and is bordered by Algeria to the west and southwest, Libya to the southeast, and the Mediterranean Sea to the north and east; covering 163,610 sq km (63,170 sq mi), with a population of 11 million. It contains the eastern end of the Atlas Mountains and the northern reaches of the Sahara desert, with much of its remaining territory arable land. Its 1,300 km (810 mi) of coastline include the African conjunction of the western and eastern parts of the Mediterranean Basin.",inline=False)  
  embed.add_field(name="Capital",value="Tunis",inline=False)
  embed.add_field(name="Flag",value="<:flag_tn:969871143383212042>",inline=False)
  embed.add_field(name="Population",value="11.70",inline=False)
  embed.add_field(name="GDP (PPP)",value="$159.70 billion",inline=False)
  embed.add_field(name="Currency",value="Tunisian dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1",inline=False)
  embed.add_field(name="Dialing Code",value="+216",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Turkey(ctx):
  embed=discord.Embed(title="Turkey",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Turkey, officially the Republic of Turkey (Turkish: Türkiye Cumhuriyeti [ˈtyɾcije dʒumˈhuːɾijeti]), is a transcontinental country located mainly on Anatolia in Western Asia, with a portion on the Balkans in Southeast Europe. It shares borders with Greece and Bulgaria to the northwest; the Black Sea to the north; Georgia to the northeast; Armenia, Azerbaijan, and Iran to the east; Iraq to the southeast; Syria and the Mediterranean Sea to the south; and the Aegean Sea to the west. Cyprus is located off the south coast. Turks form the vast majority of the nation's population and Kurds are the largest minority.",inline=False)  
  embed.add_field(name="Capital",value="Ankara",inline=False)
  embed.add_field(name="Flag",value="<:flag_tr:969871725200302132>",inline=False)
  embed.add_field(name="Population",value="84.68",inline=False)
  embed.add_field(name="GDP (PPP)",value="$3.21 trillion",inline=False)
  embed.add_field(name="Currency",value="Turkish lira",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+90",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Turkmenistan(ctx):
  embed=discord.Embed(title="Turkmenistan",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Turkmenistan, also known as Turkmenia, is a landlocked country in Central Asia, bordered by Kazakhstan to the northwest, Uzbekistan to the north, east and northeast, Afghanistan to the southeast, Iran to the south and southwest and the Caspian Sea to the west. Ashgabat is the capital and largest city of the country. The population of the country is about 6 million, the lowest of the Central Asian republics.",inline=False)  
  embed.add_field(name="Capital",value="Ashgabat",inline=False)
  embed.add_field(name="Flag",value="<:flag_tm:969872234514612304>",inline=False)
  embed.add_field(name="Population",value="6.03",inline=False)
  embed.add_field(name="GDP (PPP)",value="$112.65 million",inline=False)
  embed.add_field(name="Currency",value="Turkmenistan manat",inline=False)
  embed.add_field(name="Time Zone",value="UTC +5",inline=False)
  embed.add_field(name="Dialing Code",value="+993",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Tuvalu(ctx):
  embed=discord.Embed(title="Tuvalu",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Tuvalu, is an island country in the Polynesian subregion of Oceania in the Pacific Ocean. Its islands are situated about midway between Hawaii and Australia. They lie east-northeast of the Santa Cruz Islands (which belong to the Solomon Islands), northeast of Vanuatu, southeast of Nauru, south of Kiribati, west of Tokelau, northwest of Samoa and Wallis and Futuna, and north of Fiji. Tuvalu is composed of three reef islands and six atolls. They are spread out between the latitude of 5° and 10° south and between the longitude of 176° and 180°. They lie west of the International Date Line. Tuvalu has a population of 10,507 (2017 census). The total land area of the islands of Tuvalu is 26 square kilometres (10 sq mi).",inline=False)  
  embed.add_field(name="Capital",value="Funafuti",inline=False)
  embed.add_field(name="Flag",value="<:flag_tv:969873011165495344>",inline=False)
  embed.add_field(name="Population",value="11,900",inline=False)
  embed.add_field(name="GDP (PPP)",value="$39 million",inline=False)
  embed.add_field(name="Currency",value="Tuvaluan dollar or Australian dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +12",inline=False)
  embed.add_field(name="Dialing Code",value="+688",inline=False)
  await ctx.send(embed=embed)  
  
  

#Countries starting with U
@client.command()
async def Uganda(ctx):
  embed=discord.Embed(title="Uganda",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Uganda,  officially the Republic of Uganda (Swahili: Jamhuri ya Uganda[11]), is a landlocked country in East Africa. The country is bordered to the east by Kenya, to the north by South Sudan, to the west by the Democratic Republic of the Congo, to the south-west by Rwanda, and to the south by Tanzania. The southern part of the country includes a substantial portion of Lake Victoria, shared with Kenya and Tanzania. Uganda is in the African Great Lakes region. Uganda also lies within the Nile basin and has a varied but generally a modified equatorial climate. It has a population of over 42 million, of which 8.5 million live in the capital and largest city of Kampala.",inline=False)  
  embed.add_field(name="Capital",value="Kampala",inline=False)
  embed.add_field(name="Flag",value="<:flag_ug:969947568643657768>",inline=False)
  embed.add_field(name="Population",value="42.72 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$126.52 million",inline=False)
  embed.add_field(name="Currency",value="Ugandan shilling",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+256",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Ukraine(ctx):
  embed=discord.Embed(title="Ukraine",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Ukraine is a country in Eastern Europe. It is the second largest country in Europe after Russia, which borders it to the east and north-east. Ukraine also shares borders with Belarus to the north; Poland, Slovakia, and Hungary to the west; Romania and Moldova to the south; and has a coastline along the Sea of Azov and the Black Sea. It covers about 600,000 sq km (230,000 sq mi), with a population of about 40 million. The nation's capital and largest city is Kyiv. The official and national language is Ukrainian, and most people are also fluent in Russian.",inline=False)  
  embed.add_field(name="Capital",value="Kyiv",inline=False)
  embed.add_field(name="Flag",value="<:flag_ua:969948538136059944>",inline=False)
  embed.add_field(name="Population",value="41.16 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$584 million",inline=False)
  embed.add_field(name="Currency",value="Hryvnia",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2 or UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+380",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def UAE(ctx):
  embed=discord.Embed(title="United Arab Emirates",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="United Arab Emirates, or simply the Emirates (Arabic: الإمارات al-ʾImārāt), is a country in Western Asia. It is located at the eastern end of the Arabian Peninsula, and shares borders with Oman and Saudi Arabia, while having maritime borders in the Persian Gulf with Qatar and Iran. Abu Dhabi is the nation's capital, while Dubai, the most populous city, is an international hub.",inline=False)  
  embed.add_field(name="Capital",value="Abu Dhabi",inline=False)
  embed.add_field(name="Flag",value="<:flag_ae:969949961225662465>",inline=False)
  embed.add_field(name="Population",value="9.28 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$726.39 million",inline=False)
  embed.add_field(name="Currency",value="UAE dirham",inline=False)
  embed.add_field(name="Time Zone",value="UTC +4",inline=False)
  embed.add_field(name="Dialing Code",value="+971",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def UnitedKingdom(ctx):
  embed=discord.Embed(title="United Kingdom",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="The United Kingdom of Great Britain and Northern Ireland, commonly known as the United Kingdom (UK) or Britain,[note 1][19] is a sovereign country in north-western Europe, off the north western coast of the European mainland. The United Kingdom includes the island of Great Britain, the north eastern part of the island of Ireland, and many smaller islands within the British Isles.[22] Northern Ireland shares a land border with the Republic of Ireland. Otherwise, the United Kingdom is surrounded by the Atlantic Ocean, with the North Sea to the east, the English Channel to the south and the Celtic Sea to the south-west, giving it the 12th-longest coastline in the world. The Irish Sea separates Great Britain and Ireland. The total area of the United Kingdom is 93,628 square miles (242,500 sq km), with an estimated population in 2020 of over 67 million.",inline=False)  
  embed.add_field(name="Capital",value="London",inline=False)
  embed.add_field(name="Flag",value="<:flag_gb:969952211876593715>",inline=False)
  embed.add_field(name="Population",value="67.08 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$3.75 trillion",inline=False)
  embed.add_field(name="Currency",value="Pound sterling",inline=False)
  embed.add_field(name="Time Zone",value="UTC or UTC +1",inline=False)
  embed.add_field(name="Dialing Code",value="+44",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def UnitedStates(ctx):
  embed=discord.Embed(title="United States",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="The United States of America (U.S.A. or USA), commonly known as the United States (U.S. or US) or simply America, is a country primarily located in North America. It consists of 50 states, a federal district, five major unincorporated territories, 326 Indian reservations, and nine minor outlying islands. At nearly 3.8 million square miles (9.8 million square kilometers), it is the world's fourth-largest country by land area and third-largest by total area. The United States shares land borders with Canada to the north and Mexico to the south as well as maritime borders with the Bahamas, Cuba, and Russia, among others.",inline=False)  
  embed.add_field(name="Capital",value="Washington, D.C.",inline=False)
  embed.add_field(name="Flag",value="<:flag_us:969952940800483338>",inline=False)
  embed.add_field(name="Population",value="331.89 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$25.35 trillion",inline=False)
  embed.add_field(name="Currency",value="U.S. dollar",inline=False)
  embed.add_field(name="Dialing Code",value="+1",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Uruguay(ctx):
  embed=discord.Embed(title="United States",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Uruguay, officially the Oriental Republic of the Uruguay (Spanish: República Oriental del Uruguay), is a country in South America. It shares borders with Argentina to its west and southwest and Brazil to its north and northeast; while bordering the Río de la Plata to the south and the Atlantic Ocean to the southeast. Uruguay covers an area of approximately 176,000 square kilometers (68,000 sq mi) and has a population of an estimated 3.51 million, of whom 2 million live in the metropolitan area of its capital and largest city, Montevideo.",inline=False)  
  embed.add_field(name="Capital",value="Montevideo",inline=False)
  embed.add_field(name="Flag",value="<:flag_uy:969953931222478899>",inline=False)
  embed.add_field(name="Population",value="3.51 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$86.56 billion",inline=False)
  embed.add_field(name="Currency",value="Uruguayan peso",inline=False)
  embed.add_field(name="Dialing Code",value="+598",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Uzbekistan(ctx):
  embed=discord.Embed(title="Uzbekistan",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Uzbekistan, officially the Republic of Uzbekistan (Uzbek: Oʻzbekiston Respublikasi), is a doubly landlocked country in Central Asia. It is surrounded by five landlocked countries: Kazakhstan to the north; Kyrgyzstan to the northeast; Tajikistan to the southeast; Afghanistan to the south; and Turkmenistan to the south-west. Its capital and largest city is Tashkent. Uzbekistan is part of the Turkic languages world, as well as a member of the Organization of Turkic States. Uzbek language is the majority-spoken language in Uzbekistan.",inline=False)  
  embed.add_field(name="Capital",value="Tashkent",inline=False)
  embed.add_field(name="Flag",value="<:flag_uz:969954408949497866>",inline=False)
  embed.add_field(name="Population",value="35.30 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$335.80 billion",inline=False)
  embed.add_field(name="Currency",value="Uzbek som",inline=False)
  embed.add_field(name="Dialing Code",value="+998",inline=False)
  await ctx.send(embed=embed)  
  
  
 


#Countries Starting with V
@client.command()
async def Vanuatu(ctx):
  embed=discord.Embed(title="Vanuatu",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Vanuatu, officially the Republic of Vanuatu (French: République de Vanuatu; Bislama: Ripablik blong Vanuatu), is an island country located in the South Pacific Ocean. The archipelago, which is of volcanic origin, is 1,750 km (1,090 mi) east of northern Australia, 540 km (340 mi) northeast of New Caledonia, east of New Guinea, southeast of the Solomon Islands, and west of Fiji.",inline=False)  
  embed.add_field(name="Capital",value="Port Vila",inline=False)
  embed.add_field(name="Flag",value="<:flag_vu:970278423098458146>",inline=False)
  embed.add_field(name="Population",value="307,815",inline=False)
  embed.add_field(name="GDP (PPP)",value="$820 million",inline=False)
  embed.add_field(name="Currency",value="Vatu",inline=False)
  embed.add_field(name="Time Zone",value="UTC +11",inline=False)
  embed.add_field(name="Dialing Code",value="+678",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def VaticanCity(ctx):
  embed=discord.Embed(title="Vatican City",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Vatican City, officially the Vatican City State (Italian: Stato della Città del Vaticano; Latin: Status Civitatis Vaticanae), is an independent city-state and enclave surrounded by Rome, Italy. The Vatican City State, also known simply as the Vatican, became independent from Italy with the Lateran Treaty (1929), and it is a distinct territory under full ownership, exclusive dominion, and sovereign authority and jurisdiction of the Holy See, itself a sovereign entity of international law, which maintains the city state's temporal, diplomatic, and spiritual independence. With an area of 49 hectares (121 acres) and a population of about 825, it is the smallest state in the world by both area and population.",inline=False)  
  embed.add_field(name="Capital",value="None",inline=False)
  embed.add_field(name="Flag",value="<:flag_va:970279475294117888>",inline=False)
  embed.add_field(name="Population",value="453",inline=False)
  embed.add_field(name="Currency",value="Euro",inline=False)
  embed.add_field(name="Time Zone",value="UTC +1 or UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+379",inline=False)
  await ctx.send(embed=embed)


                  
@client.command()
async def Venezuela(ctx):
  embed=discord.Embed(title="Venezuela",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Venezuela, officially the Bolivarian Republic of Venezuela (Spanish: República Bolivariana de Venezuela), is a country on the northern coast of South America, consisting of a continental landmass and many islands and islets in the Caribbean Sea. It has a territorial extension of 916,445 sq km (353,841 sq mi), and its population was estimated at 28 million in 2019. The capital and largest urban agglomeration is the city of Caracas.",inline=False)  
  embed.add_field(name="Capital",value="Caracas",inline=False)
  embed.add_field(name="Flag",value="<:flag_ve:970280335646539776>",inline=False)
  embed.add_field(name="Population",value="28.88 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$141.94 billion",inline=False)
  embed.add_field(name="Currency",value="Venezuelan bolivar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -4",inline=False)
  embed.add_field(name="Dialing Code",value="+58",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def Vietnam(ctx):
  embed=discord.Embed(title="Vietnam",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Vietnam, officially the Socialist Republic of Vietnam, is a country in Southeast Asia. Located at the eastern edge of mainland Southeast Asia, it covers 311,699 square kilometres. With a population of over 96 million, it is the world's fifteenth-most populous country. Vietnam borders China to the north, Laos and Cambodia to the west, and shares maritime borders with Thailand through the Gulf of Thailand, and the Philippines, Indonesia, and Malaysia through the South China Sea. Its capital is Hanoi and its largest city is Ho Chi Minh City.",inline=False)  
  embed.add_field(name="Capital",value="Ho Chi Minh City",inline=False)
  embed.add_field(name="Flag",value="<:flag_vn:970281520000553000>",inline=False)
  embed.add_field(name="Population",value="96.20 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$1.04 trillion",inline=False)
  embed.add_field(name="Currency",value="dong",inline=False)
  embed.add_field(name="Time Zone",value="UTC +7",inline=False)
  embed.add_field(name="Dialing Code",value="+84",inline=False)
  await ctx.send(embed=embed)



#Countries starting with Y
@client.command()
async def Yemen(ctx):
  embed=discord.Embed(title="Yemen",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Yemen, officially the Republic of Yemen (Arabic: ٱلْجُمْهُورِيَّةُ ٱلْيَمَنِيَّةُ, romanized: al-Jumhūrīyah al-Yamanīyah, lit. 'the Yemeni Republic'), is a country in Western Asia, on the southern end of the Arabian Peninsula. It borders Saudi Arabia to the north and Oman to the northeast and shares maritime borders with Eritrea, Djibouti, Somaliland and Somalia. It is the second-largest Arab sovereign state in the peninsula, occupying 555,000 square kilometres (214,000 square miles). The coastline stretches for about 2,000 kilometres (1,200 miles). Yemen's constitutionally stated capital, and largest city, is the city of Sanaa. As of 2021, the population of the country is estimated at 30,491,000.",inline=False)  
  embed.add_field(name="Capital",value="Sanaa",inline=False)
  embed.add_field(name="Flag",value="<:flag_ye:970282382852775996>",inline=False)
  embed.add_field(name="Population",value="30.49 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$65.60 billion",inline=False)
  embed.add_field(name="Currency",value="Yemeni rial",inline=False)
  embed.add_field(name="Time Zone",value="UTC +3",inline=False)
  embed.add_field(name="Dialing Code",value="+967",inline=False)
  await ctx.send(embed=embed)


#Countries Starting with Z
@client.command()
async def Zambia(ctx):
  embed=discord.Embed(title="Zambia",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Zambia, officially the Republic of Zambia is a landlocked country at the crossroads of Central, Southern and East Africa, although it is typically referred to as being in South-Central Africa. Its neighbours are the Democratic Republic of the Congo to the north, Tanzania to the north-east, Malawi to the east, Mozambique to the southeast, Zimbabwe and Botswana to the south, Namibia to the southwest, and Angola to the west. The capital city of Zambia is Lusaka, located in the south-central part of Zambia. The population is concentrated mainly around Lusaka in the south and the Copperbelt Province to the north, the core economic hubs of the country.",inline=False)  
  embed.add_field(name="Capital",value="Lusaka",inline=False)
  embed.add_field(name="Flag",value="<:flag_zm:970283323303800892>",inline=False)
  embed.add_field(name="Population",value="17.35 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$75.85 billion",inline=False)
  embed.add_field(name="Currency",value="Zambian kwacha",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+260",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def Zimbabwe(ctx):
  embed=discord.Embed(title="Zimbabwe",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="Zimbabwe, officially the Republic of Zimbabwe, is a landlocked country located in Southeast Africa, between the Zambezi and Limpopo Rivers, bordered by South Africa to the south, Botswana to the south-west, Zambia to the north, and Mozambique to the east. The capital and largest city is Harare. The second largest city is Bulawayo. A country of roughly 15 million people, Zimbabwe has 16 official languages, with English, Shona, and Ndebele the most common. It was once known as the Jewel of Africa for its great prosperity.",inline=False)  
  embed.add_field(name="Capital",value="Harare",inline=False)
  embed.add_field(name="Flag",value="<:flag_zw:970284191549911140>",inline=False)
  embed.add_field(name="Population",value="15.09 million",inline=False)
  embed.add_field(name="GDP (PPP)",value="$38.07 billion",inline=False)
  embed.add_field(name="Currency",value="Zimbabwean dollar and U.S. dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC +2",inline=False)
  embed.add_field(name="Dialing Code",value="+263",inline=False)
  await ctx.send(embed=embed)


#Extras
@client.command()
async def Niue(ctx):
  embed=discord.Embed(title="Niue",color=discord.Colour.orange())
  embed.add_field(name="Basic Info",value="Niue is an island country in the South Pacific Ocean, 2,400 kilometres (1,500 mi) northeast of New Zealand. Niue's land area is about 261 square kilometres (101 sq mi) and its population, predominantly Polynesian, was about 1,600 in 2016. Niue is located in a triangle between Tonga, Samoa, and the Cook Islands. It is 604 kilometers northeast of Tonga.",inline=False)  
  embed.add_field(name="Capital",value="Alofi",inline=False)
  embed.add_field(name="Flag",value="<:flag_nu:970287510892728340>",inline=False)
  embed.add_field(name="Population",value="1,620",inline=False)
  embed.add_field(name="GDP (PPP)",value="$10 million",inline=False)
  embed.add_field(name="Currency",value="New Zealand dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -11",inline=False)
  embed.add_field(name="Dialing Code",value="+683",inline=False)
  await ctx.send(embed=embed)



@client.command()
async def CookIslands(ctx):
  embed=discord.Embed(title="Cook Islands",color=discord.Colour.orange())
  embed.add_field(name="Basic Info",value="The Cook Islands is a self-governing island country in the South Pacific Ocean in free association with New Zealand. It comprises 15 islands whose total land area is 240 square kilometres (93 sq mi). The Cook Islands' Exclusive Economic Zone (EEZ) covers 1,960,027 square kilometres (756,771 sq mi) of ocean.",inline=False)  
  embed.add_field(name="Capital",value="Avarua",inline=False)
  embed.add_field(name="Flag",value="<:flag_ck:970288261463429180>",inline=False)
  embed.add_field(name="Population",value="17,459",inline=False)
  embed.add_field(name="GDP (nominal)",value="$384 billion",inline=False)
  embed.add_field(name="Currency",value="New Zealand dollar",inline=False)
  embed.add_field(name="Time Zone",value="UTC -10",inline=False)
  embed.add_field(name="Dialing Code",value="+682",inline=False)
  await ctx.send(embed=embed)




  
  
keep_alive()
TOKEN=os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
