# Inferred coding style for Mediocre and Tuxedo Labs game(s)

From this image, we can see some of the teardown source code:

![Enp6CdbXUAI7dK_](https://github.com/Smashing-Tech/docs/assets/73200930/4fe2f348-a72e-4534-93c2-9d2dc61b4b07)

It is likely some of these conventions translate to Mediocre games as well, especially since they are by one person with lots of exprience and likely are more consistent.

## File names

File names are always lowercase, and don't conain underscores or seperators, even with more than one word. `.cpp` is for C++ files and `.h` is for headers in either C or C++.

## Code snippet

Here is an attempt at translating the code snippet in the image:

```cpp
		//Voxel to be checked in world space
		TVec3 wa = aToWorld.toParentPoint(la);
		
		//Voxel to be checked in other shapes local space
		TVec3 bPos = aToB.toParentPoint(la);
		
		TVec3 bPosTarget = aToBTarget.toParentPoint(la);
		????????tion????????????Square??????????????arge;
		if (????onSo???LimitS????)
		{
			//Do a ??? trace ??? the ??? voxel
			int steps = ?????? sqrt(m??????o)??????VOXEL_SIZE????
			??eps(?????????, steps);
			TVec3 bPosStart = bPos;
			for (int s = 1; s <= steps; s++)
			{
				TVec3 bPos = InterpolateLinear(bPosStart??P??ar??? | (?????? steps));
				int bx, ??????
				??->getIndexUnsafe(bPos, bx, by, bz);
				
				if (bx < 0 || bx >= vb->)mSizeX || by < 0 || by >= vb->mSizeY || bz < 0 || bz >= /*cut off*/ )
					continue;
				
				int i2 = ?????->m???????b-??????? by*vb->mSizeX ????
				
				unsigned char c2 = vb->mCollisionData[i2] & 64;
				
				if (COLLISION_CLASS[c2] == CLASS_INTERIOR)
					continue;
				
				if (edge && COLLISION_CLASS[c2] != CLASS_EDGE)
					continue;
				
				// .. cut off at end .. //
			}
		}
```
