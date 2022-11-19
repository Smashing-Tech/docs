# Physics Library

Smash Hit uses a low level physics library created by Dennis Gustafsson [[Source](https://blog.voxagon.se/2014/04/03/smashing-tech.html)].

While not much research has been done, the library appears to work on the level of algorithms rather than objects. For example, there is a class `TdGjk` with a few methods that use the GJK distance algorithm.

## Classes

 * [`TdVec3`](TdVec3.md)
 * [`TdConstraintTypeAngular`](TdConstraintTypeAngular.md)
 * [`TdConstraintTypeContact`](TdConstraintTypeContact.md)
 * [`TdConstraintTypeContactStatic`](TdConstraintTypeContactStatic.md)
 * [`TdConstraintTypeLinear`](TdConstraintTypeLinear.md)
 * [`TdConstraintTypeBase<T1, T2>`](TdConstraintTypeBase.md)
 * [`TdContextInternal`](TdContextInternal.md)
 * [`TdCso`](TdCso.md)
 * [`TdEpa`](TdEpa.md)
 * [`TdGjk`](TdGjk.md)
 * [`TdMpr`](TdMpr.md)
 * [`TdSolver`](TdSolver.md)

## Functions

### Bodies

 * tdBodyApplyImpulse
 * tdBodySetMassAsBox
 * tdBodySetMassAsInfiniteInertia
 * tdBodySetMassAsSphere
 * tdBoundingBoxAabb

### Contexts

 * tdContextCreate
 * tdContextDestroy
 * tdContextSetMaxIterations
 * tdContextSetTolerance

### Shapes

 * tdShapecast
 * tdShapeInitBox
 * tdShapeInitCapsule
 * tdShapeInitCone
 * tdShapeInitCylinder
 * tdShapeInitHull
 * tdShapeInitSphere
 * tdShapeSupport

### Solver

 * tdSolverCreate
 * tdSolverDestroy
 * tdSolverDisable
 * tdSolverEnable
 * tdSolverGetAngAcc
 * tdSolverGetIterationCount
 * tdSolverGetLinAcc
 * tdSolverGetParam
 * tdSolverInsertAngular
 * tdSolverInsertBody
 * tdSolverInsertContactBB
 * tdSolverInsertLinear
 * tdSolverInsertParticle
 * tdSolverIntegratePos
 * tdSolverIntegrateVel
 * tdSolverIsEnabled
 * tdSolverPopState
 * tdSolverPushState
 * tdSolverReset
 * tdSolverResetState
 * tdSolverSetAngAcc
 * tdSolverSetIterationCount
 * tdSolverSetLinAcc
 * tdSolverSetParam
 * tdSolverSolveConstraints
 * tdSolverStep
 * tdSolverWriteBack

### Scene

 * tdDistance
 * tdManifold
 * tdOverlap
 * tdRaycast
 * tdSupportGeneric

### Transforms

 * tdTransformInit
 * tdTransformInitM16
 * tdTransformInitP
 * tdTransformInitPQ
